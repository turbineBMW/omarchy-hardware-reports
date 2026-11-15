# Hardware report: HP HP OmniBook X Laptop 14-kr1xxx

| | |
|---|---|
| Manufacturer | HP |
| Product | HP OmniBook X Laptop 14-kr1xxx |
| SKU | D33Y9UA#ABA |
| Family | 103C_5335M8 HP OmniBook X |
| Version | ConfigID |
| Baseboard | HP 8F46 |
| Firmware | Qualcomm Technologies Inc., Insyde Inc. F.04 (03/19/2026) |
| Processor | Snapdragon(R) X2 Plus - X2P42100 - Qualcomm Oryon(TM) CPU |
| Panel | SDC4213 |
| Windows | Windows 11 Core 26H1 (build 28000.3501, Arm64) |
| Report | 5202d43e, 2026-11-15, tool 1.2.0 |

## Hardware IDs (CHIDs)

```
   0 MFPS--BvRr-- 40622e1a-aade-52a8-82c2-6c41dafd9408
   1 MFP---BvRr-- c0c25c53-403c-5bfe-bb9d-b33453445272
   2 M-P---BvRr-- 102c8ebd-6335-5972-a0bb-315c7cd4a565
   3 MFPSmp------ c670a299-d233-5486-a9b8-e38247f6698b
   4 MFPS-------- d411f91d-8f4e-50e3-8048-899da9b5ed1e
   5 MFP--------- 32e8ad3c-cf93-59ea-8d91-bf669cacda2d
   6 M--Smp------ 937bcf47-6a53-56a5-8e7e-fd08337f4c11
   7 M--S-------- c93fa3f8-11c7-586c-b067-0c09b31a2e93
   8 M-P-mp------ 1b0c3ef7-5a70-57fc-a9c0-43881f2b49e7
   9 M-P--------- 91fdd587-2367-54e2-af3a-f7f699580cec
  10 MF--mp------ aa949864-0304-5cec-9104-57c85b68875a
  11 MF---------- 5d43face-6ba8-5d41-8914-12f3410bbcf9
  12 M---------e- f999e8e2-2bed-5ee7-85be-a69096b9544d
  13 M---mp------ 9c4d99de-ba59-506d-a7b5-ffb5b3615f8a
  14 M----------- 93f84748-c854-5d6b-b78a-13c2361e0758
ext0 MFP--------E ab4bb574-f8f0-5ea4-95b6-e06e3105151d
ext1 MF---------E db598a56-34fc-5990-9e86-5320bcb38dad
ext2 M--S-------E a8d1885b-9aaa-5c65-a65b-f78de72cd99c
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 21 ACPI tables (facp, dsdt, ssdt1, ssdt2, ssdt3, apic, bert, bgrt, csrt, dbg2, facs, fpdt, gtdt, iort, mcfg, pptt, sdev, spcr, tpm2, uefi, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 260 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them. Binary values are base64.
- `firmware.json`: 284 firmware files in 184 driver packages (the devices' drivers and the extension packages applied to them, marked `extension`), by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 184 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 3664 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
- `windows.json`: what Windows' tools report: the storage bus and disks, the battery, the power states the firmware offers (`powercfg /a`), the GPU and display modes, network adapters, thermal zones, the TPM, and every third-party package in the driver store.

## Left out for privacy

- System serial number
- System UUID
- Baseboard serial number
- Baseboard asset tag
- Chassis serial number
- Chassis asset tag
- Processor serial number
- Memory serial numbers
- Memory asset tags
- Battery serial number
- SoC serial number in the ACPI tables (SOSN)
- Display serial numbers in EDID
- MSDM ACPI table (holds the Windows product key)
- 21 Bluetooth, printer, drive, network and audio-endpoint devices
- USB serial numbers and MAC addresses in device IDs
- Serial numbers and the system UUID, wherever else they appear
- 13 registry values and properties named as serial numbers, addresses or identifiers
