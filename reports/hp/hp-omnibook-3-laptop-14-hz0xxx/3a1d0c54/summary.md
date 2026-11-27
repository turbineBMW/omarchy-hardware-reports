# Hardware report: HP HP OmniBook 3 Laptop 14-hz0xxx

| | |
|---|---|
| Manufacturer | HP |
| Product | HP OmniBook 3 Laptop 14-hz0xxx |
| SKU | D34G6UAR#ABA |
| Family | 103C_5335KV HP OmniBook 3 |
| Version | ConfigID |
| Baseboard | HP 8EF1 |
| Firmware | Insyde F.02 (03/02/2026) |
| Processor | Snapdragon(R) X - X126100 - Qualcomm(R) Oryon(TM) CPU |
| Panel | AUOE3BA |
| Windows | Windows 11 Core 25H2 (build 26200.8246, Arm64) |
| Report | 3a1d0c54, 2026-11-14, tool 1.2.0 |

## Hardware IDs (CHIDs)

```
   0 MFPS--BvRr-- 97c44f7b-e43b-5ae0-a648-099cccdd884f
   1 MFP---BvRr-- ece6be7e-0dfd-5217-8205-3df2f0936f48
   2 M-P---BvRr-- c85880d7-daba-5556-ae84-0e306d44da53
   3 MFPSmp------ e0660fe0-2675-581e-994a-f48a96ae6453
   4 MFPS-------- 871c13ef-da13-5b04-8bdb-f0153f4adb22
   5 MFP--------- 686b3feb-0e15-51c5-bf0b-4bc7a64b5c12
   6 M--Smp------ 55966ad4-e29d-55a6-9106-5e925dc305e2
   7 M--S-------- b158dbe5-293d-5d6c-9075-12b4fa7b1074
   8 M-P-mp------ a863f05d-bdf8-5b5d-ac2b-5c6311b5b50a
   9 M-P--------- 3dc651a6-959e-53dd-baa6-f9ab149add34
  10 MF--mp------ e309dfb0-9a40-5a2c-ac21-10cbb8388872
  11 MF---------- 84465c77-1158-5d29-95ac-d9583b616b99
  12 M---------e- f999e8e2-2bed-5ee7-85be-a69096b9544d
  13 M---mp------ 4e2e0f04-aab5-5f36-9f30-4af6c717b877
  14 M----------- 93f84748-c854-5d6b-b78a-13c2361e0758
ext0 MFP--------E fcc69051-b644-594d-a5ff-3f6b4887dc80
ext1 MF---------E 99802180-53ba-5dce-ba59-f30df3387d4e
ext2 M--S-------E 8e0a9f04-2f78-5a74-873e-0084d8a532c7
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 20 ACPI tables (facp, dsdt, ssdt1, ssdt2, ssdt3, apic, bgrt, csrt, dbg2, facs, fpdt, gtdt, iort, mcfg, pptt, sdev, spcr, tpm2, uefi, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 249 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them. Binary values are base64.
- `firmware.json`: 288 firmware files in 165 driver packages (the devices' drivers and the extension packages applied to them, marked `extension`), by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 165 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 3415 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
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
- 14 Bluetooth, printer, drive, network and audio-endpoint devices
- USB serial numbers and MAC addresses in device IDs
- Serial numbers and the system UUID, wherever else they appear
- 13 registry values and properties named as serial numbers, addresses or identifiers
