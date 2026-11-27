# Hardware report: SAMSUNG ELECTRONICS CO., LTD. Galaxy Book Go 5G

| | |
|---|---|
| Manufacturer | SAMSUNG ELECTRONICS CO., LTD. |
| Product | Galaxy Book Go 5G |
| SKU | GALAXY A5A5-PAKL |
| Family | Galaxy Book Series |
| Version | 2.1 |
| Baseboard | SAMSUNG ELECTRONICS CO., LTD. NP545XLA-KA1TM |
| Firmware | SAMSUNG ELECTRONICS CO., LTD. P00AKL.048.251111.WY.1229 (11/11/2025) |
| Processor | Snapdragon (TM) 8cx Gen 2 @ 3.15 GHz |
| Panel | BOE07D3 |
| Windows | Windows 11 Core 25H2 (build 26200.9457, Arm64) |
| Report | dbf72fb1, 2026-11-16, tool 1.2.0 |

## Hardware IDs (CHIDs)

```
   0 MFPS--BvRr-- 781d6241-a53c-50a7-9400-05b1a47e400e
   1 MFP---BvRr-- 6ede6cf5-dcba-5c14-9d6e-20483a319374
   2 M-P---BvRr-- ad667504-0603-504a-9e86-88e279a692c9
   3 MFPSmp------ 41e17b79-57dd-53a3-8f2c-8c8a6a116ef7
   4 MFPS-------- dad425f3-1445-5ca3-90a2-2a69c788a49d
   5 MFP--------- 16791a5a-eab5-5733-b4d6-8276d17bb1c5
   6 M--Smp------ 58fee4f2-862e-5a88-9842-c67bd3df9d85
   7 M--S-------- bb04ea9d-135d-57f3-b28d-c6a248d68a84
   8 M-P-mp------ 4e53e38d-2a87-5c81-8359-85467acd752f
   9 M-P--------- 3bf91e20-c904-5f7f-a85a-81f96d447a80
  10 MF--mp------ e75cfdba-d5be-5247-819a-67ad119e9a9b
  11 MF---------- f139ecb6-912d-56a7-b140-9ba326833643
  12 M---------e- b5ba5e91-fdc7-52c1-85b5-9a0da49c298f
  13 M---mp------ 5d6f0c97-881a-5f94-8264-deb12ceac70f
  14 M----------- ca0158e4-038b-5a84-8037-1b3cbf948d8a
ext0 MFP--------E 82d13252-829e-5bb6-acdf-dfad0572b8d3
ext1 MF---------E 75b2b451-8127-5458-a93a-488b82fa320c
ext2 M--S-------E 497bbccd-c59e-5594-8ab7-b98a584a756e
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 14 ACPI tables (facp, dsdt, apic, bgrt, csrt, dbg2, facs, fpdt, gtdt, iort, mcfg, pptt, tpm2, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 242 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them. Binary values are base64.
- `firmware.json`: 371 firmware files in 157 driver packages (the devices' drivers and the extension packages applied to them, marked `extension`), by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 157 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 4140 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
- `windows.json`: what Windows' tools report: the storage bus and disks, the battery, the power states the firmware offers (`powercfg /a`), the GPU and display modes, network adapters, thermal zones, the TPM, and every third-party package in the driver store.

## Left out for privacy

- System serial number
- System UUID
- Memory serial numbers
- Memory asset tags
- Chassis serial number
- Chassis asset tag
- Baseboard serial number
- Baseboard asset tag
- SoC serial number in the ACPI tables (SOSN)
- Display serial numbers in EDID
- MSDM ACPI table (holds the Windows product key)
- 72 Bluetooth, printer, drive, network and audio-endpoint devices
- USB serial numbers and MAC addresses in device IDs
- Serial numbers and the system UUID, wherever else they appear
- 12 registry values and properties named as serial numbers, addresses or identifiers
