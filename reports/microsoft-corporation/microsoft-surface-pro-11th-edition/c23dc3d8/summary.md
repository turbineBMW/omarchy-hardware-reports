# Hardware report: Microsoft Corporation Microsoft Surface Pro, 11th Edition

| | |
|---|---|
| Manufacturer | Microsoft Corporation |
| Product | Microsoft Surface Pro, 11th Edition |
| SKU | Surface_Pro_11th_Edition_2076 |
| Family | Surface |
| Version | 124I:00117T:000M:0000000F:0B:09C:12M:02D:00U:12T:2R:21 |
| Baseboard | Microsoft Corporation Microsoft Surface Pro, 11th Edition |
| Firmware | Microsoft Corporation 175.449.235 (08/05/2026) |
| Processor | Snapdragon(R) X 12-core X1E80100 @ 3.40 GHz |
| Panel | SDC4195 |
| Windows | Windows 11 Core 26H2 (build 26300.9711, Arm64) |
| Report | c23dc3d8, 2026-11-11, tool 1.0.0 |

## Hardware IDs (CHIDs)

```
   0 MFPS--BvRr-- 1cba3d89-9e86-5c9c-9bab-417d135f3850
   1 MFP---BvRr-- 68be5d65-c360-5c82-9416-a3c39775aab0
   2 M-P---BvRr-- 9bef7ab8-b62a-5610-94b7-4095808b544c
   3 MFPSmp------ aca467c0-5fc2-59ad-8ed5-1b7a0988d11c
   4 MFPS-------- 95971fb3-d478-591f-9ea3-eb0af0d1dfb5
   5 MFP--------- c9c14db9-2b61-597a-a4ba-84397fe75f63
   6 M--Smp------ 7cef06f5-e7e6-56d7-b123-a6d640a5d302
   7 M--S-------- 48b86a5e-1955-5799-9577-150f9e1a69e4
   8 M-P-mp------ 06128fee-87dc-50f6-8a3f-97cd9a6d8bf6
   9 M-P--------- 84b2e1d1-e695-5f41-8c41-cf1f059c616a
  10 MF--mp------ 16a47337-1f8b-5bd3-b3bd-8e50b31cb1c9
  11 MF---------- ca2e5189-1d32-509f-88a0-d4ebcc721899
  12 M---------e- aca387a9-183e-5da9-8f9d-f460c3f50f54
  13 M---mp------ fdef4ae0-6bfb-5706-8aae-a565639505f5
  14 M----------- cc0aea32-ad2c-5013-8bed-cede6be8c9f4
ext0 MFP--------E d752a22b-1fd8-53c3-89ef-8ca95618134a
ext1 MF---------E ca2ff828-b404-5253-9e0e-579c93bfb059
ext2 M--S-------E 65bc7507-3ca6-5afa-9ea1-9fd1c099a3e7
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 17 ACPI tables (facp, dsdt, ssdt, apic, bgrt, csrt, dbg2, facs, fpdt, gtdt, iort, mcfg, pptt, sdev, spcr, tpm2, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 311 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them. Binary values are base64.
- `firmware.json`: 112 firmware files in 174 driver packages, by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 174 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 3805 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
- `windows.json`: what Windows' tools report: the storage bus and disks, the battery, the power states the firmware offers (`powercfg /a`), the GPU and display modes, network adapters, thermal zones, the TPM, and every third-party package in the driver store.

## Left out for privacy

- SoC serial number in the ACPI tables (SOSN)
- Processor serial number
- System serial number
- System UUID
- Chassis serial number
- Baseboard serial number
- Display serial numbers in EDID
- MSDM ACPI table (holds the Windows product key)
- 103 Bluetooth, printer, drive, network and audio-endpoint devices
- USB serial numbers and MAC addresses in device IDs
- Serial numbers and the system UUID, wherever else they appear
- 14 registry values and properties named as serial numbers, addresses or identifiers
