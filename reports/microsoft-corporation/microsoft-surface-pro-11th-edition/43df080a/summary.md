# Hardware report: Microsoft Corporation Microsoft Surface Pro, 11th Edition

| | |
|---|---|
| Manufacturer | Microsoft Corporation |
| Product | Microsoft Surface Pro, 11th Edition |
| SKU | Surface_Pro_11th_Edition_2076 |
| Family | Surface |
| Version | 124I:00117T:000M:0000000F:0B:08C:10M:02D:11U:09T:2R:21 |
| Baseboard | Microsoft Corporation Microsoft Surface Pro, 11th Edition |
| Firmware | Microsoft Corporation 175.222.235 (02/23/2026) |
| Processor | Snapdragon(R) X 10-core X1P64100 @ 3.40 GHz |
| Panel | LGD077B |
| Windows | Windows 11 Core 25H2 (build 26200.9168, Arm64) |
| Report | 43df080a, 2026-11-08, tool 1.1.0 |

## Hardware IDs (CHIDs)

```
   0 MFPS--BvRr-- fdc6d8ba-ec50-546e-a3c0-62a5f58116c7
   1 MFP---BvRr-- c5c1df9c-209b-59e6-bfac-bb5409d2daa5
   2 M-P---BvRr-- 4403a531-07b3-512b-8976-f4aa73287449
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
ext0 MFP--------E 2a0f2d6c-3aa0-5386-9d6e-0ddbfa0eeb94
ext1 MF---------E 5003998f-4753-59a4-85d4-e62b9c30a421
ext2 M--S-------E 2245edda-fd9b-5703-a77a-39a91bf64878
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 17 ACPI tables (facp, dsdt, ssdt, apic, bgrt, csrt, dbg2, facs, fpdt, gtdt, iort, mcfg, pptt, sdev, spcr, tpm2, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 303 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them. Binary values are base64.
- `firmware.json`: 446 firmware files in 218 driver packages (the devices' drivers and the extension packages applied to them, marked `extension`), by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 218 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 3641 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
- `windows.json`: what Windows' tools report: the storage bus and disks, the battery, the power states the firmware offers (`powercfg /a`), the GPU and display modes, network adapters, thermal zones, the TPM, and every third-party package in the driver store.

## Left out for privacy

- Processor serial number
- System serial number
- System UUID
- Chassis serial number
- Baseboard serial number
- SoC serial number in the ACPI tables (SOSN)
- Display serial numbers in EDID
- MSDM ACPI table (holds the Windows product key)
- 74 Bluetooth, printer, drive, network and audio-endpoint devices
- USB serial numbers and MAC addresses in device IDs
- Serial numbers and the system UUID, wherever else they appear
- 6 registry values and properties named as serial numbers, addresses or identifiers
