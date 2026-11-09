# Hardware report: Microsoft Corporation Microsoft Surface Laptop, 7th Edition

| | |
|---|---|
| Manufacturer | Microsoft Corporation |
| Product | Microsoft Surface Laptop, 7th Edition |
| SKU | Surface_Laptop_7th_Edition_2036 |
| Family | Surface |
| Version | 124I:00108T:000M:0000000F:0B:10C:10M:01D:05U:03T:2R:21S:0A:0 |
| Baseboard | Microsoft Corporation Microsoft Surface Laptop, 7th Edition |
| Firmware | Microsoft Corporation 175.327.235 (06/24/2026) |
| Processor | Snapdragon(R) X 10-core X1P64100 @ 3.40 GHz |
| Panel | SHP1572 |
| Windows | Windows 11 Core 26H2 (build 26300.9711, Arm64) |
| Report | 21ab1011, 2026-11-09, tool 1.1.0 |

## Hardware IDs (CHIDs)

```
   0 MFPS--BvRr-- 2369bae8-c8b5-5d54-8a5f-84ffa4bced80
   1 MFP---BvRr-- b1157bdf-595b-5239-b0e7-8a94539125ce
   2 M-P---BvRr-- fdf0f38f-1f3f-5a83-b3a3-ed297e2f138a
   3 MFPSmp------ fdfca0f3-41b6-5872-a2ea-53539fd5160c
   4 MFPS-------- 11696377-327d-5ad1-b01d-02a7dbb9b99a
   5 MFP--------- 892e90c9-31e3-5131-a217-a02632dba5e9
   6 M--Smp------ 786c71b6-f60e-51c7-9ddc-f2999b75a3c5
   7 M--S-------- f0d12ad9-f530-5b56-96d8-897dd704059e
   8 M-P-mp------ 3c329240-a447-5ec5-b79b-d1149420ac62
   9 M-P--------- 224ba2ff-14c1-5b33-ac10-079ccc217be2
  10 MF--mp------ 924900a0-9be2-53ca-90d7-b0e38827f5c5
  11 MF---------- ca2e5189-1d32-509f-88a0-d4ebcc721899
  12 M---------e- aca387a9-183e-5da9-8f9d-f460c3f50f54
  13 M---mp------ 1c07beb2-8442-5086-baab-2c44a468e3a3
  14 M----------- cc0aea32-ad2c-5013-8bed-cede6be8c9f4
ext0 MFP--------E 3ae9fa68-43f6-56d8-b701-f6596ec0cc1a
ext1 MF---------E 8e474443-cd10-5105-a1ea-59f46e8c0c69
ext2 M--S-------E 324be12d-b22a-50b1-ac2b-7faa757388d8
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 17 ACPI tables (facp, dsdt, ssdt, apic, bgrt, csrt, dbg2, facs, fpdt, gtdt, iort, mcfg, pptt, sdev, spcr, tpm2, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 280 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them; 1 without a working driver. Binary values are base64.
- `firmware.json`: 411 firmware files in 210 driver packages (the devices' drivers and the extension packages applied to them, marked `extension`), by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 210 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 3736 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
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
- 37 Bluetooth, printer, drive, network and audio-endpoint devices
- USB serial numbers and MAC addresses in device IDs
- Serial numbers and the system UUID, wherever else they appear
- 13 registry values and properties named as serial numbers, addresses or identifiers
