# Hardware report: LENOVO 83N3

| | |
|---|---|
| Manufacturer | LENOVO |
| Product | 83N3 |
| SKU | LENOVO_MT_83N3_BU_idea_FM_IdeaPad Slim 3 15Q8X10 |
| Family | IdeaPad Slim 3 15Q8X10 |
| Version | IdeaPad Slim 3 15Q8X10 |
| Baseboard | LENOVO LNVNB161216 |
| Firmware | LENOVO RVCN35WW (09/15/2026) |
| Processor | Snapdragon(R) X - X126100 - Qualcomm(R) Oryon(TM) CPU |
| Panel | LEN9191 |
| Windows | Windows 11 Core 26H2 (build 26300.9974, Arm64) |
| Report | 85c9358e, 2026-11-21, tool 1.3.0 |

## Hardware IDs (CHIDs)

```
   0 MFPS--BvRr-- 3bd743d0-5b67-58d4-97b5-08834b520eb9
   1 MFP---BvRr-- 9a64b8d6-a26b-5525-ae5f-042c1b2fb753
   2 M-P---BvRr-- 817f051e-a853-5331-a5d2-bf9438c21933
   3 MFPSmp------ 4f6c85c4-b6e2-5cd9-9a22-91b839f31474
   4 MFPS-------- 0549a586-ab3b-5606-a55a-f9374515909c
   5 MFP--------- 1bee74fc-5f4d-53a1-92a3-f532d4170a95
   6 M--Smp------ b59e5273-1ed4-51d7-9beb-da0e48f96459
   7 M--S-------- 123d7adb-792e-5e3e-9044-3d5eec53b59d
   8 M-P-mp------ 67f92433-2c48-5d27-8423-afe79c8f86e1
   9 M-P--------- 0b1ba81f-8f6b-5ba3-aebc-a6e71b280d83
  10 MF--mp------ f9f59b59-b3f3-5b8a-a65a-84bc573ee694
  11 MF---------- 216c17d6-9f5b-5020-b8cc-1be8b74f6204
  12 M---------e- e093d715-70f7-51f4-b6c8-b4a7e31def85
  13 M---mp------ 71d86d4d-02f8-5566-a7a1-529cef184b7e
  14 M----------- 6de5d951-d755-576b-bd09-c5cf66b27234
ext0 MFP--------E b7966a78-e947-5c35-8020-3b9516a88a01
ext1 MF---------E a2211a28-36ac-5055-bc0a-679ae36442b4
ext2 M--S-------E a5eb7272-1afd-55f1-ac20-75372d939d23
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 18 ACPI tables (facp, dsdt, ssdt, apic, bgrt, csrt, dbg2, facs, fft_, fpdt, gtdt, iort, mcfg, pptt, spcr, tpm2, uefi, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 252 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them. Binary values are base64.
- `firmware.json`: 341 firmware files in 171 driver packages (the devices' drivers and the extension packages applied to them, marked `extension`), by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 171 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 3430 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
- `windows.json`: what Windows' tools report: the storage bus and disks, the battery, the power states the firmware offers (`powercfg /a`), the GPU and display modes, network adapters, thermal zones, the TPM, and every third-party package in the driver store.

## Left out for privacy

- System serial number
- System UUID
- Baseboard serial number
- Baseboard asset tag
- Chassis serial number
- Chassis asset tag
- Processor serial number
- Battery serial number
- SoC serial number in the ACPI tables (SOSN)
- Display serial numbers in EDID
- MSDM ACPI table (holds the Windows product key)
- 19 Bluetooth, printer, drive, network and audio-endpoint devices
- USB serial numbers and MAC addresses in device IDs
- Serial numbers and the system UUID, wherever else they appear
- 14 registry values and properties named as serial numbers, addresses or identifiers
