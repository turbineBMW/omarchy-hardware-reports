# Hardware report: HP HP OmniBook 5 Laptop 14-he0xxx

| | |
|---|---|
| Manufacturer | HP |
| Product | HP OmniBook 5 Laptop 14-he0xxx |
| SKU | C08Q7PA#ACJ |
| Family | 103C_5335KV HP OmniBook 5 |
| Version | ConfigID |
| Baseboard | HP 8E33 |
| Firmware | Insyde F.05 (09/02/2025) |
| Processor | Snapdragon(R) X - X126100 - Qualcomm(R) Oryon(TM) CPU |
| Panel | SDC4212 |
| Windows | Windows 11 Home Single Language 24H2 (build 26100.9711, Arm64) |
| Report | 97863638, 2026-11-09, tool 1.1.0-manual-powershell |

## Hardware IDs (CHIDs)

```
0    MFPS--BvRr-- 09255343-9fc7-5dac-b784-457b1561226a
1    MFP---BvRr-- 99fdba8b-38d1-5bd0-abc7-e83617adf4ed
2    M-P---BvRr-- 9dfdbe1e-0c6b-50e5-823b-b0dd4f3a6b6f
3    MFPSmp------ b9b3eafa-ec80-5cd8-93b8-4242cb8d5e2b
4    MFPS-------- 52fafd85-126d-560b-91ba-ef4dd9803f1d
5    MFP--------- 16908eb8-2d8a-5dde-a6a6-8d22238b078a
6    M--Smp------ 315c6fa8-2434-5eb5-ba67-4024e4041c9a
7    M--S-------- 71fa78eb-680b-5082-b519-389e7fb4eb93
8    M-P-mp------ 9f15eae2-29db-5d55-9627-840fe41e3ec0
9    M-P--------- 860c9fd7-bb87-59da-b2d8-a38c5dec1188
10   MF--mp------ 33f1c4d6-5df6-5d6c-9f15-421865586185
11   MF---------- b95e57c6-0395-526b-a79e-003c982210c5
12   M---------e- f999e8e2-2bed-5ee7-85be-a69096b9544d
13   M---mp------ f96424b4-fb7e-5822-95c8-8ffe76c2e740
14   M----------- 93f84748-c854-5d6b-b78a-13c2361e0758
ext0 MFP--------E 2c8ad3d1-2be6-56da-bc3e-45f60c91954c
ext1 MF---------E 64f59956-aadf-5943-80fc-1e0e09481764
ext2 M--S-------E 65789177-df29-582f-9d36-6ede3a505ed9
```

Fields: M manufacturer, F family, P product, S SKU, m/p baseboard manufacturer/product, B/v/R/r BIOS vendor/version/major/minor, e enclosure, E panel EDID.

## Contents

- `acpi/`: 20 ACPI tables (facp, dsdt, ssdt1, ssdt2, ssdt3, apic, bgrt, csrt, dbg2, fpdt, gtdt, iort, mcfg, pptt, sdev, spcr, tpm2, uefi, xsdt, facs). Disassemble with `iasl -d acpi/dsdt.dat`.
- `smbios/dmi.bin`: the SMBIOS table; read it with `dmidecode --from-dump smbios/dmi.bin`.
- `edid/`: display EDIDs.
- `devices.json`: 265 devices with hardware IDs, ACPI paths, drivers and every property pnputil exposes; binary values as base64.
- `firmware.json`: firmware and other files in the devices' driver packages, by name, size and SHA256.
- `windows.json`: what Windows' tools say about storage, battery, power states, thermal zones, displays, the TPM and the driver store.
- `registry/`: the registry keys the hardware descriptions come from (Enum and driver keys per device, related services, and the system branches with the SMBIOS mirror).
- `drivers/`: the driver packages' INF files.

## Collector note

Collected manually with a read-only .NET collector (registry, WMI/CIM, pnputil, GetSystemFirmwareTable). The official Omarchy Arm Installer executable is blocked by Smart App Control (enforcement) on this machine and the owner chose to keep Smart App Control enabled, so the report was gathered by hand.
Differences from tool 1.1.0 output: custom GUID-form device properties beyond pnputil's named set are not captured; Device_Stack is not synthesized; powerCapabilities/powerSchemes mirror `powercfg` text lines as keys; extension INF flags come from pnputil's Extension class.
