# Hardware report: Acer Aspire A14-11M

| | |
|---|---|
| Manufacturer | Acer |
| Product | Aspire A14-11M |
| SKU | 0000000000000000 |
| Family | Aspire 14 AI |
| Version | 6.0 |
| Baseboard | SX1 Tiguan_SX1 |
| Firmware | Insyde Corp. V1.10 (04/29/2026) |
| Processor | Snapdragon(R) X - X126100 - Qualcomm(R) Oryon(TM) CPU |
| Panel | CSW1458 |
| Windows | Windows 11 Enterprise 26H2 (build 26300.9818, Arm64) |
| Report | b914f61c, 2026-10-30, tool 1.0.0 |

## Hardware IDs (CHIDs)

```
   0 MFPS--BvRr-- 8b9dc4ba-a93e-5189-aa04-6805c6fd735f
   1 MFP---BvRr-- abd888a9-990c-5a66-8f50-3344e7c76fcf
   2 M-P---BvRr-- 00788fb3-dbe8-5954-94d2-3dd9cddbd7f6
   3 MFPSmp------ dd65a519-9cb1-5fb1-acb9-f8b914368f6a
   4 MFPS-------- 430ccde2-3c1b-5a09-9874-d582fda39c19
   5 MFP--------- 823bcf3d-2b07-55bc-92ad-bf9e8c033f40
   6 M--Smp------ daa59d3d-14d0-55d9-840c-a80d34b26ba2
   7 M--S-------- 9625cffd-3b14-56dc-aa6f-c768e6dbf160
   8 M-P-mp------ 18ac5b4c-3598-5199-a1ae-954b0e3b3efc
   9 M-P--------- 00d64345-2d46-58ca-aaa0-032613b7b8cd
  10 MF--mp------ 5bc6b3ba-200a-5943-9609-fad249299ada
  11 MF---------- e443e193-ae25-5084-92d5-77b830486278
  12 M---------e- 92dcc94d-48f7-5ee8-b9ec-a6393fb7a484
  13 M---mp------ 807d3810-7703-5b12-be96-8018e1aa5cf9
  14 M----------- 1e301734-5d49-5df4-9ed2-aa1c0a9dddda
ext0 MFP--------E 4573a934-1c4c-5ae5-a2d8-74767cb36cfe
ext1 MF---------E 8211f8a7-faf0-551c-bfc1-67afc33f1316
ext2 M--S-------E f41166e5-4a0b-52b0-96b4-2287203709aa
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 18 ACPI tables (facp, dsdt, ssdt, apic, bgrt, csrt, dbg2, facs, fpdt, gtdt, iort, mcfg, pptt, sdev, spcr, tpm2, uefi, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 266 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them; 1 without a working driver. Binary values are base64.
- `firmware.json`: 117 firmware files in 163 driver packages, by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 163 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 3478 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
- `windows.json`: what Windows' tools report: the storage bus and disks, the battery, the power states the firmware offers (`powercfg /a`), the GPU and display modes, network adapters, thermal zones, the TPM, and every third-party package in the driver store.

## Left out for privacy

- System serial number
- System UUID
- Baseboard serial number
- Baseboard asset tag
- Chassis serial number
- Chassis asset tag
- Processor serial number
- Display serial numbers in EDID
- MSDM ACPI table (holds the Windows product key)
- 29 Bluetooth, printer, drive, network and audio-endpoint devices
- USB serial numbers and MAC addresses in device IDs
- Serial numbers and the system UUID, wherever else they appear
- 19 registry values and properties named as serial numbers, addresses or identifiers
