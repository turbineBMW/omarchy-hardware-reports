# Hardware report: HP HP OmniBook 3 Laptop 16-bz0xxx

| | |
|---|---|
| Manufacturer | HP |
| Product | HP OmniBook 3 Laptop 16-bz0xxx |
| SKU | CQ1M7UA#ABA |
| Family | 103C_5335KV HP OmniBook 3 |
| Version | ConfigID |
| Baseboard | HP 8EE6 |
| Firmware | Insyde F.06 (08/06/2026) |
| Processor | Snapdragon(R) X - X126100 - Qualcomm(R) Oryon(TM) CPU |
| Panel | AUOD7B5 |
| Windows | Windows 11 Core 26H2 (build 26300.9711, Arm64) |
| Report | 6cff1e36, 2026-11-05, tool 1.0.1 |

## Hardware IDs (CHIDs)

```
   0 MFPS--BvRr-- 5589d4e3-b6b6-5687-baa5-1d41359674de
   1 MFP---BvRr-- 7f27f702-d531-5536-b5d3-8fcfcf7b5409
   2 M-P---BvRr-- 002e1741-544b-53ce-9908-32c5807ec301
   3 MFPSmp------ 49b4ab3f-62f5-56b4-ba81-978c5073ef3c
   4 MFPS-------- b64faaeb-bc4b-55e6-ae39-69b4e0ddc7cb
   5 MFP--------- bc2007a5-78ce-5e00-8f56-af55b083bd69
   6 M--Smp------ f9b943c5-95bb-56c8-ae80-9b28e5dd5170
   7 M--S-------- 4a8965ba-59c7-5e8a-89dc-4e9176579608
   8 M-P-mp------ 54c75dff-89ed-5e18-974b-209e4dcf15ae
   9 M-P--------- b69f7f62-0ab1-5dc1-9290-a732246a6add
  10 MF--mp------ 99d095d0-4514-5c03-bfed-a6e17f882f66
  11 MF---------- 84465c77-1158-5d29-95ac-d9583b616b99
  12 M---------e- f999e8e2-2bed-5ee7-85be-a69096b9544d
  13 M---mp------ 3545c64d-cf8a-55a9-bc4e-b227c3c04d54
  14 M----------- 93f84748-c854-5d6b-b78a-13c2361e0758
ext0 MFP--------E 81127a29-bb2a-5cde-aa7a-3d05b083326f
ext1 MF---------E f5404785-f537-5676-80e9-7291217f1b27
ext2 M--S-------E c83d2314-a406-5861-a0e0-39a337da1f96
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 20 ACPI tables (facp, dsdt, ssdt1, ssdt2, ssdt3, apic, bgrt, csrt, dbg2, facs, fpdt, gtdt, iort, mcfg, pptt, sdev, spcr, tpm2, uefi, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 237 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them. Binary values are base64.
- `firmware.json`: 292 firmware files in 173 driver packages (the devices' drivers and the extension packages applied to them, marked `extension`), by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 173 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 3467 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
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
- 49 Bluetooth, printer, drive, network and audio-endpoint devices
- USB serial numbers and MAC addresses in device IDs
- Serial numbers and the system UUID, wherever else they appear
- 14 registry values and properties named as serial numbers, addresses or identifiers
