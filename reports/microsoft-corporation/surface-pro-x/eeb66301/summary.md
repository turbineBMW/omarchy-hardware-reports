# Hardware report: Microsoft Corporation Surface Pro X

| | |
|---|---|
| Manufacturer | Microsoft Corporation |
| Product | Surface Pro X |
| SKU | Surface_Pro_X_1876 |
| Family | Surface |
| Version | 124I:00045T:000M:0400000B:07 |
| Baseboard | Microsoft Corporation Surface Pro X |
| Firmware | Microsoft Corporation 4.234.140 (04/30/2025) |
| Processor | Microsoft SQ1 @ 3.0 GHz |
| Panel | LGD0555 |
| Windows | Windows 11 Professional 26H2 (build 26300.9818, Arm64) |
| Report | eeb66301, 2026-11-15, tool 1.2.0 |

## Hardware IDs (CHIDs)

```
   0 MFPS--BvRr-- f5d079fd-4e60-5338-b10b-6efd40f0a288
   1 MFP---BvRr-- 2c760338-2ea3-5462-81ae-297cd95ad2ba
   2 M-P---BvRr-- e0709fd5-2800-554c-b8f9-18b1400f6052
   3 MFPSmp------ 21c23c53-98d5-5f92-8e8b-60bbea3509fe
   4 MFPS-------- 1dc8ec42-9eeb-51b1-9490-0cb33bd7d23a
   5 MFP--------- cc2bc434-a08a-59c0-85ac-2576ed611de6
   6 M--Smp------ cfd77e02-45cc-5a46-9102-bf5881241933
   7 M--S-------- 38d5909b-b425-5db8-b533-1133e81465e8
   8 M-P-mp------ b07028e2-19c1-577d-a3c9-2eabef35c2a1
   9 M-P--------- 5d018db8-6de6-55f8-8d8b-4b773caf8450
  10 MF--mp------ db7e6e61-56bf-531d-b594-e4b1660d04aa
  11 MF---------- ca2e5189-1d32-509f-88a0-d4ebcc721899
  12 M---------e- aca387a9-183e-5da9-8f9d-f460c3f50f54
  13 M---mp------ f199ec04-d0d9-542b-b035-209532a4d1f6
  14 M----------- cc0aea32-ad2c-5013-8bed-cede6be8c9f4
ext0 MFP--------E f27bf0cf-7937-534b-8573-2b6e6ff352fb
ext1 MF---------E 2d035dcc-0dc4-5cd4-9480-1f61bfc827d9
ext2 M--S-------E c2deca53-d7d4-5d00-876c-98c5c7eb3cc2
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 15 ACPI tables (facp, dsdt, apic, bert, bgrt, csrt, dbg2, facs, fpdt, gtdt, iort, mcfg, pptt, tpm2, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 298 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them. Binary values are base64.
- `firmware.json`: 268 firmware files in 193 driver packages (the devices' drivers and the extension packages applied to them, marked `extension`), by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 193 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 3624 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
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
- 32 Bluetooth, printer, drive, network and audio-endpoint devices
- USB serial numbers and MAC addresses in device IDs
- Serial numbers and the system UUID, wherever else they appear
- 19 registry values and properties named as serial numbers, addresses or identifiers
