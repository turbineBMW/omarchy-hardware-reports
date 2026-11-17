# Hardware report: ASUSTeK COMPUTER INC. ASUS Vivobook S 14 S3407QA_S3407QA

| | |
|---|---|
| Manufacturer | ASUSTeK COMPUTER INC. |
| Product | ASUS Vivobook S 14 S3407QA_S3407QA |
| Family | ASUS Vivobook S 14 |
| Version | 1.0 |
| Baseboard | ASUSTeK COMPUTER INC. S3407QA |
| Firmware | Insyde S3407QA.311 (05/22/2026) |
| Processor | Snapdragon(R) X - X126100 - Qualcomm(R) Oryon(TM) CPU |
| Panel | NCP0061 |
| Windows | Windows 11 Core 26H2 (build 26300.9974, Arm64) |
| Report | a7d05faf, 2026-11-17, tool 1.2.0 |

## Hardware IDs (CHIDs)

```
   1 MFP---BvRr-- 083492bc-caa3-5198-b662-ebb6b334bd7c
   2 M-P---BvRr-- 537022b5-74c9-5326-b56b-08f119103eee
   5 MFP--------- 21413277-589d-570d-85d3-70a7311794b2
   8 M-P-mp------ 1deb1b04-b39b-510c-9eea-610da0691489
   9 M-P--------- c9e04d56-5a9e-596e-bc93-0c2a3a434508
  10 MF--mp------ 0b25878a-5ef5-5cfb-a121-365686c0ca6a
  11 MF---------- 1417b199-407e-51ee-b445-84dd736e5b77
  12 M---------e- 665276be-80c5-5e5d-929f-fa85d18e2d50
  13 M---mp------ 91497d3e-0546-59c6-98a5-e65f79e7f06d
  14 M----------- 65605ed1-09e2-57aa-bd0f-a26c1d35433f
ext0 MFP--------E 1e8c254e-e554-500b-9552-70ed1d4feb4e
ext1 MF---------E 4300a5b5-6c5a-589e-9668-a7877d4e88ca
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 17 ACPI tables (facp, dsdt, apic, bgrt, csrt, dbg2, facs, fpdt, gtdt, iort, mcfg, pptt, sdev, spcr, tpm2, uefi, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 258 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them. Binary values are base64.
- `firmware.json`: 411 firmware files in 193 driver packages (the devices' drivers and the extension packages applied to them, marked `extension`), by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 193 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 3422 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
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
- 40 Bluetooth, printer, drive, network and audio-endpoint devices
- USB serial numbers and MAC addresses in device IDs
- The computer and user names, wherever they appear
- Serial numbers and the system UUID, wherever else they appear
- 15 registry values and properties named as serial numbers, addresses or identifiers
