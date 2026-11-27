# Hardware report: SAMSUNG ELECTRONICS CO., LTD. Galaxy Book4 Edge

| | |
|---|---|
| Manufacturer | SAMSUNG ELECTRONICS CO., LTD. |
| Product | Galaxy Book4 Edge |
| SKU | GALAXY A5A5-PAKX |
| Family | Galaxy Book4 Edge |
| Version | 2.1 |
| Baseboard | SAMSUNG ELECTRONICS CO., LTD. NP960XMB-KB1US |
| Firmware | SAMSUNG ELECTRONICS CO., LTD. P00AKX.068.260409.WY.1908 (04/ 9/2026) |
| Processor | Snapdragon(R) X Elite - X1E84100 - Qualcomm(R) Oryon(TM) CPU |
| Panel | SDC4188 |
| Windows | Windows 11 Enterprise 26H2 (build 26300.9818, Arm64) |
| Report | a220b319, 2026-11-09, tool 1.1.0 |

## Hardware IDs (CHIDs)

```
   0 MFPS--BvRr-- 91c24876-ebef-54f5-9f94-50a584778479
   1 MFP---BvRr-- dfc30a39-3223-5468-8565-d6615fc5fa6d
   2 M-P---BvRr-- 2c4bad6d-c1cc-5877-ba64-92975a522632
   3 MFPSmp------ adde1ac8-800d-531b-8358-335f24308e6f
   4 MFPS-------- f0353726-3e21-5ec9-ab33-d95d485c7109
   5 MFP--------- 613d0dcf-9d03-51a3-b87f-ce3fff939dd0
   6 M--Smp------ 1518cf55-bd92-5038-8add-a122b0335fe0
   7 M--S-------- e45a937a-853e-5c3b-aeb7-de037d453eab
   8 M-P-mp------ 45153613-8171-51b1-930b-8aea3ab5c055
   9 M-P--------- 0339244b-ab5d-5c54-a901-344543f4e40c
  10 MF--mp------ 45153613-8171-51b1-930b-8aea3ab5c055
  11 MF---------- 0339244b-ab5d-5c54-a901-344543f4e40c
  12 M---------e- b5ba5e91-fdc7-52c1-85b5-9a0da49c298f
  13 M---mp------ 1f0d6fd9-215c-5995-ada9-8604ecc71b52
  14 M----------- ca0158e4-038b-5a84-8037-1b3cbf948d8a
ext0 MFP--------E 2d340d6e-a493-5dc0-9735-48a0d00dba48
ext1 MF---------E a2672a02-da1b-5d69-adfb-7eff43eed6f0
ext2 M--S-------E 380fa98c-b549-54d6-a774-cef10f572520
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 14 ACPI tables (facp, dsdt, apic, bgrt, csrt, dbg2, facs, fpdt, gtdt, iort, mcfg, pptt, tpm2, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 252 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them. Binary values are base64.
- `firmware.json`: 384 firmware files in 191 driver packages (the devices' drivers and the extension packages applied to them, marked `extension`), by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 191 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 3335 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
- `windows.json`: what Windows' tools report: the storage bus and disks, the battery, the power states the firmware offers (`powercfg /a`), the GPU and display modes, network adapters, thermal zones, the TPM, and every third-party package in the driver store.

## Left out for privacy

- System serial number
- System UUID
- Memory serial numbers
- Memory asset tags
- Chassis serial number
- Chassis asset tag
- Processor serial number
- Baseboard serial number
- Baseboard asset tag
- SoC serial number in the ACPI tables (SOSN)
- Display serial numbers in EDID
- MSDM ACPI table (holds the Windows product key)
- 34 Bluetooth, printer, drive, network and audio-endpoint devices
- The computer and user names, wherever they appear
- USB serial numbers and MAC addresses in device IDs
- Serial numbers and the system UUID, wherever else they appear
- 5 registry values and properties named as serial numbers, addresses or identifiers
