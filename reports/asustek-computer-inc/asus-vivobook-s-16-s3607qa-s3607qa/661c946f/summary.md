# Hardware report: ASUSTeK COMPUTER INC. ASUS Vivobook S 16 S3607QA_S3607QA

| | |
|---|---|
| Manufacturer | ASUSTeK COMPUTER INC. |
| Product | ASUS Vivobook S 16 S3607QA_S3607QA |
| Family | ASUS Vivobook S 16 |
| Version | 1.0 |
| Baseboard | ASUSTeK COMPUTER INC. S3607QA |
| Firmware | Insyde S3607QA.311 (05/22/2026) |
| Processor | Snapdragon(R) X - X126100 - Qualcomm(R) Oryon(TM) CPU |
| Panel | BOE0D25 |
| Windows | Windows 11 Core 25H2 (build 26200.8875, Arm64) |
| Report | 661c946f, 2026-10-31, tool 1.0.0 |

## Hardware IDs (CHIDs)

```
   1 MFP---BvRr-- f2d8bff1-dd6a-5112-bbd2-055dcfc13120
   2 M-P---BvRr-- 1748d3f0-e0bb-5d80-b21f-4f4eafdb3123
   5 MFP--------- 8576477d-8266-57a6-b98c-bc229f7e4071
   8 M-P-mp------ 1126b191-7fc8-5342-b33c-d130791ebf76
   9 M-P--------- 340f9225-42fc-5329-8e1b-1506e324a80c
  10 MF--mp------ 001fc203-742f-5f7a-b22f-f9c4f575b6bf
  11 MF---------- 160ffb8b-5540-5e3f-8249-482ab4f60aa2
  12 M---------e- 665276be-80c5-5e5d-929f-fa85d18e2d50
  13 M---mp------ 9ee2d47b-9126-5b8b-ba6c-b058e5296f55
  14 M----------- 65605ed1-09e2-57aa-bd0f-a26c1d35433f
ext0 MFP--------E e3a7e4b3-3a38-5108-bcb0-f71cf0e4153c
ext1 MF---------E 422f5819-47b2-5b0a-9413-1b6012cec09c
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 17 ACPI tables (facp, dsdt, apic, bgrt, csrt, dbg2, facs, fpdt, gtdt, iort, mcfg, pptt, sdev, spcr, tpm2, uefi, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 255 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them. Binary values are base64.
- `firmware.json`: 142 firmware files in 147 driver packages, by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 147 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 3458 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
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
- Display serial numbers in EDID
- MSDM ACPI table (holds the Windows product key)
- 28 Bluetooth, printer, drive, network and audio-endpoint devices
- USB serial numbers and MAC addresses in device IDs
- Serial numbers and the system UUID, wherever else they appear
- 16 registry values and properties named as serial numbers, addresses or identifiers
