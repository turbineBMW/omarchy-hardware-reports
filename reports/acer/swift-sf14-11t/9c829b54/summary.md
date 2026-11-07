# Hardware report: Acer Swift SF14-11T

| | |
|---|---|
| Manufacturer | Acer |
| Product | Swift SF14-11T |
| SKU | 0000000000000000 |
| Family | Swift 14 AI |
| Version | 6.0 |
| Baseboard | SX1 Bluetang_SX1 |
| Firmware | Insyde Corp. V1.27 (12/10/2025) |
| Processor | Snapdragon(R) X Elite - X1E78100 - Qualcomm(R) Oryon(TM) CPU |
| Panel | AUOF3A7 |
| Windows | Windows 11 Professional 25H2 (build 26200.9711, Arm64) |
| Report | 9c829b54, 2026-11-05, tool 1.0.1 |

## Hardware IDs (CHIDs)

```
   0 MFPS--BvRr-- a50b2dc3-7665-5a92-9bc8-b389f0a4874a
   1 MFP---BvRr-- d48fd4e5-a949-5411-8630-b9e7ea381b61
   2 M-P---BvRr-- 08b0c4ba-6cc5-5752-a254-5a68cba08c6a
   3 MFPSmp------ c53429ce-93d9-5bf6-b6ef-afc52d51ef5a
   4 MFPS-------- b4bfd645-4767-5199-94f5-9dd92c91aa7d
   5 MFP--------- de75b122-a838-5e2d-9607-747f4ac3b335
   6 M--Smp------ e4134d8a-ebe7-5893-b4ef-b09bbcd8e8b3
   7 M--S-------- 9625cffd-3b14-56dc-aa6f-c768e6dbf160
   8 M-P-mp------ 72c8065a-3a24-5c3b-bec7-b2358eab98ac
   9 M-P--------- 316441f6-8cc6-5fb9-9f12-943bee4d140a
  10 MF--mp------ ee8fa049-e5f4-51e4-89d8-89a0140b8f38
  11 MF---------- 4cdff732-fd0c-5bac-b33e-9002788ea557
  12 M---------e- 92dcc94d-48f7-5ee8-b9ec-a6393fb7a484
  13 M---mp------ 32f83b0f-1fad-5be2-88be-5ab020e7a70e
  14 M----------- 1e301734-5d49-5df4-9ed2-aa1c0a9dddda
ext0 MFP--------E 5d7535f1-2e8f-573e-950a-4652ba4cfe8f
ext1 MF---------E 0a043e05-97b8-526f-9096-69272917da77
ext2 M--S-------E f0da1a1f-bd6e-566a-a5e3-6d26687ada5f
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID. The same values `systemd-analyze chid` prints; `hwids.json` is ready for systemd's `src/boot/hwids` once the device tree's compatible is filled in.

## Contents

- `acpi/`: 18 ACPI tables (facp, dsdt, ssdt, apic, bgrt, csrt, dbg2, facs, fpdt, gtdt, iort, mcfg, pptt, sdev, spcr, tpm2, uefi, xsdt). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 273 devices with hardware IDs, ACPI paths, drivers and every property the configuration manager has for them; 2 without a working driver. Binary values are base64.
- `firmware.json`: 420 firmware files in 208 driver packages (the devices' drivers and the extension packages applied to them, marked `extension`), by name, size and SHA-256, with a Microsoft Update Catalog search for each package, and the packages' other files the same way. The firmware itself is not included.
- `drivers/`: the 208 INF files of those packages, which say which device loads which firmware and what settings its driver gets.
- `registry/`: 3454 registry keys. `devices.json` holds each device's own key (Device Parameters, LogConf) and its driver's settings key under Control\Class; `services.json` the drivers' service keys; `system.json` HARDWARE\DESCRIPTION\System (processors, firmware, configuration data), DEVICEMAP, RESOURCEMAP (the memory, interrupts and bus connections each driver was given, decoded beside the raw value), SystemInformation (Windows' own CHIDs) and Secure Boot's state. Binaries over 64 KiB are in `blobs/`.
- `windows.json`: what Windows' tools report: the storage bus and disks, the battery, the power states the firmware offers (`powercfg /a`), the GPU and display modes, network adapters, thermal zones, the TPM, and every third-party package in the driver store.

## Left out for privacy

- System serial number
- System UUID
- Baseboard serial number
- Baseboard asset tag
- Chassis serial number
- Chassis asset tag
- Processor serial number
- SoC serial number in the ACPI tables (SOSN)
- Display serial numbers in EDID
- MSDM ACPI table (holds the Windows product key)
- 33 Bluetooth, printer, drive, network and audio-endpoint devices
- USB serial numbers and MAC addresses in device IDs
- Serial numbers and the system UUID, wherever else they appear
- 14 registry values and properties named as serial numbers, addresses or identifiers
