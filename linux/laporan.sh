#!/bin/bash

if [ -z "$1" ]; then
    echo "Pemakaian: ./laporan.sh namafile"
    exit 1
fi

if [ ! -f "$1" ]; then
    echo "File tidak ditemukan: $1"
    exit 1
fi

jumlah=$(wc -l < "$1")
terendah=$(sort -n "$1" | head -n 1)
tertinggi=$(sort -n "$1" | tail -n 1)

echo "Jumlah data: $jumlah"
echo "Terendah: $terendah"
echo "Tertinggi: $tertinggi"
