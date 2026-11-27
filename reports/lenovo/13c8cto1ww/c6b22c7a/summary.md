# Hardware report: LENOVO 13C8CTO1WW

| | |
|---|---|
| Manufacturer | LENOVO |
| Product | 13C8CTO1WW |
| SKU | LENOVO_MT_13C8_BU_Think_FM_ThinkCentre neo 50q QC |
| Family | ThinkCentre neo 50q QC |
| Version | ThinkCentre neo 50q QC |
| Baseboard | LENOVO 3393 |
| Firmware | LENOVO M60KT3BA (05/02/2025) |
| Processor | Snapdragon(R) X - X126100 - Qualcomm(R) Oryon(TM) CPU |
| Panel | BNQ78E6 |
| Windows | Windows 11 Professional 26H2 (build 26300.9711, Arm64) |
| Report | c6b22c7a, 2026-11-08, tool 1.1.0 |

## Hardware IDs (CHIDs)

```
   0 MFPS--BvRr-- d5da4d4a-0c03-51d6-b58f-c365e8e15eff
   1 MFP---BvRr-- 217044a3-c606-5bcb-b9c4-c243c723dd5f
   2 M-P---BvRr-- 8dcbd7fa-4549-54df-946a-f750aa15b261
   3 MFPSmp------ 7200c6a7-a129-5ad3-b60e-7bfb80367259
   4 MFPS-------- 55f7cadf-29a7-5f44-b0da-5d60db2d3d62
   5 MFP--------- a7d3802c-0b79-52ca-b0df-fce36f9d2488
   6 M--Smp------ b5330b6c-dd44-548a-ae34-4fb03d69d5f7
   7 M--S-------- 260c6642-8b04-55ec-acaf-dc4a1725d25d
   8 M-P-mp------ 9c47f1f2-1a86-5a79-b9ce-b24b9029fb76
   9 M-P--------- 48022068-676f-5db9-8495-1a786f70b5a5
  10 MF--mp------ 659761ea-dc76-506e-bdc5-38eb5d394b39
  11 MF---------- 1c1a4153-c3a4-55a6-bc6b-c939d6b3a716
  12 M---------e- 78cfbbd7-c5d4-5d24-9ad2-df6114c7d37d
  13 M---mp------ 4dc0d1e5-e2ff-5a7e-88b4-6d63b7f024a4
  14 M----------- 6de5d951-d755-576b-bd09-c5cf66b27234
ext0 MFP--------E 80f34d32-665f-527e-a17d-9b6d15348485
ext1 MF---------E de3a3d41-9cae-5a9d-868e-325517637580
ext2 M--S-------E bcfd0bfe-d961-5cb8-9170-fc395dc6762f
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 22 ACPI tables (facp, dsdt, ssdt1, ssdt2, ssdt3, ssdt4, apic, bgrt, csrt, dbg2, facs, fft_, fpdt, gtdt, iort, mcfg, pptt, spcr, tpm2, uefi, xsdt1, xsdt2). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 234 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them. Binary values are base64.
- `firmware.json`: 209 firmware files in 149 driver packages (the devices' drivers and the extension packages applied to them, marked `extension`), by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 149 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 3068 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
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
- 50 Bluetooth, printer, drive, network and audio-endpoint devices
- USB serial numbers and MAC addresses in device IDs
- Serial numbers and the system UUID, wherever else they appear
- 15 registry values and properties named as serial numbers, addresses or identifiers
