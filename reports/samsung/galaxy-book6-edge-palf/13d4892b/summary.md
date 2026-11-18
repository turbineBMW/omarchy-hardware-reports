# Hardware report: Samsung Galaxy Book6 Edge - PALF

| | |
|---|---|
| Manufacturer | Samsung |
| Product | Galaxy Book6 Edge - PALF |
| SKU | PALF-960XRD-GLYM-0 |
| Family | Galaxy Book6 Edge |
| Version | 1.0 |
| Baseboard | Samsung NP960XRD-KB1DE |
| Firmware | American Megatrends International, LLC. PALF.0.0.29.0 (03/ 5/2026) |
| Processor | Snapdragon(R) X2 Elite - X2E88100 - Qualcomm Oryon(TM) CPU |
| Panel | SDC4188 |
| Windows | Windows 11 Core 26H1 (build 28000.3501, Arm64) |
| Report | 13d4892b, 2026-11-18, tool 1.3.0 |

## Hardware IDs (CHIDs)

```
   0 MFPS--BvRr-- 1bf2dd84-0a37-5b89-be76-a6e5ee90b4f9
   1 MFP---BvRr-- d3973f0a-7058-5b80-8c10-eefd34f7a126
   2 M-P---BvRr-- 5f5016ab-b29c-52c6-b3d3-e44d26732edb
   3 MFPSmp------ 82e1a922-a0e1-5e6f-8ea6-d40e7d035c7f
   4 MFPS-------- 09be0b55-e2e6-57b0-8908-5b10bea5a34e
   5 MFP--------- 5b955977-b320-51a7-b71f-cd988db9e1d0
   6 M--Smp------ 4814ecd1-ea5b-5982-ba17-16148466197c
   7 M--S-------- ed115ea6-ab6d-510a-a6e6-3880a310b340
   8 M-P-mp------ 057b0661-0ea9-57a3-bd6f-5025d8080a66
   9 M-P--------- 558d9176-3f3d-574b-895f-869bd50c335c
  10 MF--mp------ deea9f7b-0abd-5991-a51e-b868be811cdd
  11 MF---------- 72bd00d9-0e12-574c-8536-cce54dbdb813
  12 M---------e- 3e4c6f31-fc0f-5e0f-b21f-8e3b52c17ff7
  13 M---mp------ 5b460c19-87b8-5127-9984-857fb00957ff
  14 M----------- 8fdd277a-a351-5a91-9cd4-80f321765274
ext0 MFP--------E 760af4de-8fd7-577d-ae3c-e3848d5f46c7
ext1 MF---------E ac25ca72-707c-5bdf-8b8b-96561f3b37ad
ext2 M--S-------E e72f599e-cdd7-546c-aafe-df2312faa337
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 16 ACPI tables (facp, dsdt, apic, bert, bgrt, csrt, dbg2, facs, fpdt, gtdt, iort, mcfg, pptt, spcr, tpm2, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 290 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them. Binary values are base64.
- `firmware.json`: 321 firmware files in 194 driver packages (the devices' drivers and the extension packages applied to them, marked `extension`), by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 194 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 3590 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
- `windows.json`: what Windows' tools report: the storage bus and disks, the battery, the power states the firmware offers (`powercfg /a`), the GPU and display modes, network adapters, thermal zones, the TPM, and every third-party package in the driver store.

## Left out for privacy

- System serial number
- System UUID
- Chassis serial number
- Chassis asset tag
- Processor serial number
- Baseboard serial number
- Baseboard asset tag
- SoC serial number in the ACPI tables (SOSN)
- Display serial numbers in EDID
- MSDM ACPI table (holds the Windows product key)
- 14 Bluetooth, printer, drive, network and audio-endpoint devices
- USB serial numbers and MAC addresses in device IDs
- Serial numbers and the system UUID, wherever else they appear
- 12 registry values and properties named as serial numbers, addresses or identifiers
