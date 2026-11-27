# Hardware report: ASUS ProArt PZ14 HT7407NA

| | |
|---|---|
| Manufacturer | ASUS |
| Product | ProArt PZ14 HT7407NA |
| Family | ProArt PZ14 |
| Version | 1.0        |
| Baseboard | ASUSTeK COMPUTER INC. HT7407NA |
| Firmware | Insyde HT7407NA.309 (08/20/2026) |
| Processor | Snapdragon(R) X2 Elite - X2E88100 - Qualcomm Oryon(TM) CPU |
| Panel | BOE0D7B |
| Windows | Windows 11 CoreCountrySpecific 26H1 (build 28000.3231, Arm64) |
| Report | f79c37b6, 2026-11-10, tool 1.2.0 |

## Hardware IDs (CHIDs)

```
   1 MFP---BvRr-- 893057af-0f0d-5649-8dec-f4b619285bae
   2 M-P---BvRr-- 551ba4bf-1ecc-5993-b829-2ae50f0e9b4c
   5 MFP--------- 2df5f8d3-fbd1-5af3-9168-841b376cdee0
   8 M-P-mp------ fe5f498c-9e87-54d8-96ab-66a2c20ab597
   9 M-P--------- 9a35a0bb-7b19-58ef-bc0c-6051ed101c7d
  10 MF--mp------ 58c8aa55-813e-56cd-90c7-da03a83020e9
  11 MF---------- 44e3c9d3-7f6f-5b1c-9dff-bf7dc533307b
  12 M---------e- cffb64b7-9f72-59c4-ad25-b1ed61e8a2ab
  13 M---mp------ e5040c17-eb1e-5050-a463-d6c9bafd2a8f
  14 M----------- c4e7b7b9-2520-5397-8040-8ac279f540d8
ext0 MFP--------E 910b94d0-8475-5f7b-9bf5-b6b1410a0a0b
ext1 MF---------E e36d34c5-2de6-50c8-b0a2-4497ed734912
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 18 ACPI tables (facp, dsdt, apic, bert, bgrt, csrt, dbg2, facs, fpdt, gtdt, iort, mcfg, pptt, sdev, spcr, tpm2, uefi, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 288 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them. Binary values are base64.
- `firmware.json`: 390 firmware files in 204 driver packages (the devices' drivers and the extension packages applied to them, marked `extension`), by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 204 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 3263 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
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
- 64 Bluetooth, printer, drive, network and audio-endpoint devices
- USB serial numbers and MAC addresses in device IDs
- Serial numbers and the system UUID, wherever else they appear
- 13 registry values and properties named as serial numbers, addresses or identifiers
