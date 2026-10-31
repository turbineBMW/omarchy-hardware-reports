# Hardware report: Acer Aspire A16-11M

| | |
|---|---|
| Manufacturer | Acer |
| Product | Aspire A16-11M |
| SKU | 0000000000000000 |
| Family | Aspire 16 AI |
| Version | 6.0 |
| Baseboard | SX1 Venue_SX1 |
| Firmware | Insyde Corp. V1.09 (02/26/2026) |
| Processor | Snapdragon(R) X - X126100 - Qualcomm(R) Oryon(TM) CPU |
| Panel | CSW1666 |
| Windows | Windows 11 Core 26H2 (build 26300.9711, Arm64) |
| Report | c18c6aea, 2026-10-31, tool 1.0.0 |

## Hardware IDs (CHIDs)

```
   0 MFPS--BvRr-- dbc9553e-59eb-533b-9cd4-19a066dd752c
   1 MFP---BvRr-- 7023b088-10f4-5d23-a872-c917abbc547a
   2 M-P---BvRr-- 2fb277a4-f628-5132-a7e0-bedad05a9d16
   3 MFPSmp------ 5ec0bc4a-e869-5a86-8b9d-4e0d3f2fb772
   4 MFPS-------- 6ef0d296-7047-5fab-a02c-be32249e15b9
   5 MFP--------- d3d98724-7f99-58d6-8f91-bcaffe9974e7
   6 M--Smp------ 83fc9383-239f-5dca-a720-e9248d9701fb
   7 M--S-------- 9625cffd-3b14-56dc-aa6f-c768e6dbf160
   8 M-P-mp------ a4f0baa5-52dd-5d58-9046-3b5d678417f4
   9 M-P--------- 82414d70-10f6-5a97-beab-dd51d1bcf49f
  10 MF--mp------ 427c626c-b3ad-577a-ac5b-241e599600ca
  11 MF---------- 2cbcdb24-25ec-51da-829a-05c8df55f201
  12 M---------e- 92dcc94d-48f7-5ee8-b9ec-a6393fb7a484
  13 M---mp------ 7c78c197-19db-53e2-b774-faf8b47f6498
  14 M----------- 1e301734-5d49-5df4-9ed2-aa1c0a9dddda
ext0 MFP--------E 97e7cc8c-2530-5b3c-b2d6-3d7d3171b290
ext1 MF---------E 2cf3330a-bf90-5d24-b93a-114a3e9df031
ext2 M--S-------E 0a516b7b-15ef-5e3d-8f18-6df5a958691f
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 18 ACPI tables (facp, dsdt, ssdt, apic, bgrt, csrt, dbg2, facs, fpdt, gtdt, iort, mcfg, pptt, sdev, spcr, tpm2, uefi, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 258 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them. Binary values are base64.
- `firmware.json`: 116 firmware files in 164 driver packages, by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 164 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 3675 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
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
- 42 Bluetooth, printer, drive, network and audio-endpoint devices
- The computer and user names, wherever they appear
- USB serial numbers and MAC addresses in device IDs
- Serial numbers and the system UUID, wherever else they appear
- 14 registry values and properties named as serial numbers, addresses or identifiers
