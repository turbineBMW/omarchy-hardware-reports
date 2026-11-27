# Hardware report: Dell Inc. Inspiron 14 5441

| | |
|---|---|
| Manufacturer | Dell Inc. |
| Product | Inspiron 14 5441 |
| SKU | 0C84 |
| Family | Inspiron |
| Baseboard | Dell Inc. 0DGG6Y |
| Firmware | Dell Inc. 2.16.0 (07/ 9/2026) |
| Processor | Snapdragon(R) X Plus - X1P42100 - Qualcomm(R) Oryon(TM) CPU |
| Panel | CSW143D |
| Windows | Windows 11 Core 26H2 (build 26300.9711, Arm64) |
| Report | c4e26892, 2026-11-09, tool 1.1.0 |

## Hardware IDs (CHIDs)

```
   0 MFPS--BvRr-- 43b00bf1-051a-55cf-8aa6-4e0d424e1a52
   1 MFP---BvRr-- 38c0b930-f178-5f14-9a14-00d3e13e431b
   2 M-P---BvRr-- 8f809737-324b-5bb4-9d24-cc32eef86849
   3 MFPSmp------ 3d8cd946-63d3-5ec7-8ebf-211a41be8d3e
   4 MFPS-------- 2d64da22-4984-5a97-8d25-f27e4794e196
   5 MFP--------- 90eab468-ac3a-5857-bac2-606a088a539b
   6 M--Smp------ 292909ae-0328-5ee8-b965-f8d64266ea1f
   7 M--S-------- 8dd6ba4a-10ab-594e-95c5-aa78f81c0621
   8 M-P-mp------ f110a06d-0540-5b88-9dab-25f4f1f2073d
   9 M-P--------- 924908db-a80b-5fff-8917-7e9b79e933eb
  10 MF--mp------ 11c02816-fd4f-554c-945d-06331bb5089a
  11 MF---------- 717bca8b-c237-5776-9736-3922a63c6938
  12 M---------e- 5c163113-9296-5c8d-a92d-ae04eb59a0f7
  13 M---mp------ 402dea86-8a39-50fc-84b4-2e373e1bb25a
  14 M----------- 85d38fda-fc0e-5c6f-808f-076984ae7978
ext0 MFP--------E d4a5a661-003a-5777-9dd2-bbf81fe92027
ext1 MF---------E 3776b0d2-1eba-5ba7-acc0-fdfc4ac16fb1
ext2 M--S-------E 70cb5ae4-a979-54b7-82e8-4307cccadc4b
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 16 ACPI tables (facp, dsdt, apic, bgrt, csrt, dbg2, facs, fpdt, gtdt, iort, mcfg, pptt, sdev, spcr, tpm2, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 234 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them; 1 without a working driver. Binary values are base64.
- `firmware.json`: 323 firmware files in 168 driver packages (the devices' drivers and the extension packages applied to them, marked `extension`), by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 168 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 3266 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
- `windows.json`: what Windows' tools report: the storage bus and disks, the battery, the power states the firmware offers (`powercfg /a`), the GPU and display modes, network adapters, thermal zones, the TPM, and every third-party package in the driver store.

## Left out for privacy

- Processor serial number
- Battery serial number
- System serial number
- System UUID
- Baseboard serial number
- Chassis serial number
- SoC serial number in the ACPI tables (SOSN)
- Display serial numbers in EDID
- MSDM ACPI table (holds the Windows product key)
- 15 Bluetooth, printer, drive, network and audio-endpoint devices
- The computer and user names, wherever they appear
- USB serial numbers and MAC addresses in device IDs
- Serial numbers and the system UUID, wherever else they appear
- 5 registry values and properties named as serial numbers, addresses or identifiers
