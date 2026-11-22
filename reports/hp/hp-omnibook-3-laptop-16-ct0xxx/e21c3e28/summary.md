# Hardware report: HP HP OmniBook 3 Laptop 16-ct0xxx

| | |
|---|---|
| Manufacturer | HP |
| Product | HP OmniBook 3 Laptop 16-ct0xxx |
| SKU | E0VU0UA#ABL |
| Family | 103C_5335KV HP OmniBook 3 |
| Baseboard | HP 8FD0 |
| Firmware | AMI F.03 (10/09/2026) |
| Processor | Snapdragon(R) C - C110100 - Qualcomm(R) Kryo(TM) CPU |
| Panel | TMA2109 |
| Windows | Windows 11 Core 26H2 (build 26300.10075, Arm64) |
| Report | e21c3e28, 2026-11-22, tool 1.3.0 |

## Hardware IDs (CHIDs)

```
   0 MFPS--BvRr-- c7c70490-4a13-5d35-8832-6b954b84b884
   1 MFP---BvRr-- 1af03614-7c98-59b9-92ee-3b65783c51f0
   2 M-P---BvRr-- 9be6abc4-a0c0-5845-8e91-229dc6101bfe
   3 MFPSmp------ cdb242cb-4d3f-5c2f-a53c-2a3d1cacc0e5
   4 MFPS-------- 5eff0eae-71a2-5342-8b39-6df029f3282c
   5 MFP--------- b267efb4-aa5f-5791-8ff0-46b63ec8d0d1
   6 M--Smp------ fdb0248f-bf2c-5884-8724-8eecadc219b6
   7 M--S-------- 61095d7d-9a77-5169-a276-ef604ca88e60
   8 M-P-mp------ 6c3203da-52cb-58c9-9f35-ed8330856ce1
   9 M-P--------- 121b925d-79f6-5f99-8ac8-e4c87721fce4
  10 MF--mp------ fe677703-82d5-509f-a5e9-e9120cb05b31
  11 MF---------- 84465c77-1158-5d29-95ac-d9583b616b99
  12 M---------e- f999e8e2-2bed-5ee7-85be-a69096b9544d
  13 M---mp------ 52038437-1029-5b77-b413-740ca929bb81
  14 M----------- 93f84748-c854-5d6b-b78a-13c2361e0758
ext0 MFP--------E aa6aabc1-159d-5330-9248-e374fd32cbc4
ext1 MF---------E e43d369a-46f4-5751-bea8-1e89e96b335d
ext2 M--S-------E 1a7fd50c-3a81-5b8e-a4f8-8f21648fdd72
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 16 ACPI tables (facp, dsdt, apic, bgrt, csrt, dbg2, facs, fpdt, gtdt, iort, mcfg, pptt, spcr, tpm2, wsmt, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 202 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them. Binary values are base64.
- `firmware.json`: 218 firmware files in 138 driver packages (the devices' drivers and the extension packages applied to them, marked `extension`), by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 138 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 2557 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
- `windows.json`: what Windows' tools report: the storage bus and disks, the battery, the power states the firmware offers (`powercfg /a`), the GPU and display modes, network adapters, thermal zones, the TPM, and every third-party package in the driver store.

## Left out for privacy

- System serial number
- System UUID
- Baseboard serial number
- Baseboard asset tag
- Chassis serial number
- Battery serial number
- Memory serial numbers
- Memory asset tags
- Processor serial number
- SoC serial number in the ACPI tables (SOSN)
- Display serial numbers in EDID
- MSDM ACPI table (holds the Windows product key)
- 13 Bluetooth, printer, drive, network and audio-endpoint devices
- USB serial numbers and MAC addresses in device IDs
- Serial numbers and the system UUID, wherever else they appear
- 4 registry values and properties named as serial numbers, addresses or identifiers
