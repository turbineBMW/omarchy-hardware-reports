# Hardware report: Anduril Qualcomm Glymur

| | |
|---|---|
| Manufacturer | Anduril |
| Product | Qualcomm Glymur |
| SKU | Qualcomm Glymur |
| Family | Qualcomm Glymur |
| Version | V0.04 |
| Baseboard | COMPAL NY4P9 |
| Firmware | Anduril V0.04 (10/08/2026) |
| Processor | Snapdragon(R) X2 Elite - X2E88100 - Qualcomm Oryon(TM) CPU |
| Panel | SDC422F |
| Windows | Windows 11 Professional 26H1 (build 28000.3231, Arm64) |
| Report | f5904cef, 2026-11-06, tool 1.0.1 |

## Hardware IDs (CHIDs)

```
   0 MFPS--BvRr-- 53d58ab3-e910-5d10-a2ec-80e051d566b8
   1 MFP---BvRr-- a9a1b83e-c434-5e61-a6aa-cce5a026419d
   2 M-P---BvRr-- 6779ed07-7f14-52d8-9535-66619531e78f
   3 MFPSmp------ 96908d9d-ae94-5809-930d-92fe88c36038
   4 MFPS-------- d57f96c5-a504-585f-9d6b-845854d720fa
   5 MFP--------- 2ac7c5d5-8318-5be4-b088-477f9a004bc1
   6 M--Smp------ 7ac534d4-a41c-53b9-87f6-c01a102082b4
   7 M--S-------- b2f01473-c24f-5adb-a1fd-eaa60da1a921
   8 M-P-mp------ 7ac534d4-a41c-53b9-87f6-c01a102082b4
   9 M-P--------- b2f01473-c24f-5adb-a1fd-eaa60da1a921
  10 MF--mp------ 7ac534d4-a41c-53b9-87f6-c01a102082b4
  11 MF---------- b2f01473-c24f-5adb-a1fd-eaa60da1a921
  12 M---------e- 4ab0b5ea-bb10-5f16-8172-a27d88939955
  13 M---mp------ d1017c92-f6cf-54fc-8bf7-0a2725a064ed
  14 M----------- 9fa2d0aa-d761-5c3c-884e-32c6b17a0d8f
ext0 MFP--------E 473ae65d-b557-5883-afcb-bd99761da7fc
ext1 MF---------E 888804a5-f928-546f-b9ac-6c06a8cf1bf0
ext2 M--S-------E 888804a5-f928-546f-b9ac-6c06a8cf1bf0
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 20 ACPI tables (facp, dsdt, ssdt, apic, bert, bgrt, csrt, dbg2, facs, fft_, fpdt, gtdt, iort, mcfg, pptt, sdev, spcr, tpm2, uefi, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 274 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them. Binary values are base64.
- `firmware.json`: 330 firmware files in 182 driver packages (the devices' drivers and the extension packages applied to them, marked `extension`), by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 182 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 3505 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
- `windows.json`: what Windows' tools report: the storage bus and disks, the battery, the power states the firmware offers (`powercfg /a`), the GPU and display modes, network adapters, thermal zones, the TPM, and every third-party package in the driver store.

## Left out for privacy

- System serial number
- System UUID
- Baseboard serial number
- Baseboard asset tag
- Chassis serial number
- Chassis asset tag
- Processor serial number
- SoC serial number in the ACPI tables (SOSN)
- Display serial numbers in EDID
- 24 Bluetooth, printer, drive, network and audio-endpoint devices
- USB serial numbers and MAC addresses in device IDs
- Serial numbers and the system UUID, wherever else they appear
- 13 registry values and properties named as serial numbers, addresses or identifiers
