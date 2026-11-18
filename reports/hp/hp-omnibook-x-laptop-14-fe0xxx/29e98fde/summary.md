# Hardware report: HP HP OmniBook X Laptop 14-fe0xxx

| | |
|---|---|
| Manufacturer | HP |
| Product | HP OmniBook X Laptop 14-fe0xxx |
| SKU | A2NZ3AS#ABA |
| Family | 103C_5335M8 HP OmniBook X |
| Version | ConfigID |
| Baseboard | HP 8CBE |
| Firmware | Insyde F.34 (06/26/2026) |
| Processor | Snapdragon(R) X Elite - X1E78100 - Qualcomm(R) Oryon(TM) CPU |
| Panel | BOE0C93 |
| Windows | Windows 11 Professional 26H2 (build 26300.9974, Arm64) |
| Report | 29e98fde, 2026-11-18, tool 1.3.0 |

## Hardware IDs (CHIDs)

```
   0 MFPS--BvRr-- 392e7951-bd76-5aa5-9e66-29f262645708
   1 MFP---BvRr-- 7510b05f-4665-5387-bb1f-1f48ca62570f
   2 M-P---BvRr-- a6194672-5acd-5787-9e03-6c2086a49003
   3 MFPSmp------ 9501cf18-9e66-526a-a318-299d6d1e3eef
   4 MFPS-------- 18217c6e-cce5-59f8-84f3-d6193e14a58e
   5 MFP--------- 811126e6-4aee-5f9e-827d-d0f12f6a6f00
   6 M--Smp------ 3bb77d90-82c6-5cb6-aeec-f00226f74ad9
   7 M--S-------- f5abafad-f55e-5ddb-8ed4-d1c3f66fb423
   8 M-P-mp------ 1a192aee-2cfd-5ab5-95f9-8093218a48ef
   9 M-P--------- eaab52c6-ed22-5e1b-b788-fc5a0531291d
  10 MF--mp------ 848aeb1d-302b-5b6b-9109-0f4632535915
  11 MF---------- 5d43face-6ba8-5d41-8914-12f3410bbcf9
  12 M---------e- f999e8e2-2bed-5ee7-85be-a69096b9544d
  13 M---mp------ 2ae478e9-ef65-5485-bb06-a233136e53c7
  14 M----------- 93f84748-c854-5d6b-b78a-13c2361e0758
ext0 MFP--------E e1514102-4ff2-584c-86c4-8c1679a8f140
ext1 MF---------E 8d089810-c832-56ae-974a-a5dd536a16b2
ext2 M--S-------E ddacb793-60bc-5ddc-bb7e-febaa8997191
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 21 ACPI tables (facp, dsdt, ssdt1, ssdt2, ssdt3, ssdt4, apic, bgrt, csrt, dbg2, facs, fpdt, gtdt, iort, mcfg, pptt, sdev, spcr, tpm2, uefi, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 243 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them; 1 without a working driver. Binary values are base64.
- `firmware.json`: 317 firmware files in 171 driver packages (the devices' drivers and the extension packages applied to them, marked `extension`), by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 171 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 3224 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
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
- 18 Bluetooth, printer, drive, network and audio-endpoint devices
- USB serial numbers and MAC addresses in device IDs
- Serial numbers and the system UUID, wherever else they appear
- 4 registry values and properties named as serial numbers, addresses or identifiers
