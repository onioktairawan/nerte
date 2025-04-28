
#  Userbot

Panduan Instalasi dan Penggunaan Vii Userbot

## Langkah 1: Update dan Upgrade Sistem
Untuk memulai, pastikan sistem kamu up-to-date dengan menjalankan perintah berikut:

```bash
apt update && apt upgrade -y
```

## Langkah 2: Clone Repository
Clone repository  Userbot dari GitHub:

```bash
git clone https://github.com/onioktairawan/serpabot
```

Masuk ke direktori `serpabot`:

```bash
cd serpabot
```

## Langkah 3: Install Dependencies
Install *FFmpeg* yang dibutuhkan untuk beberapa fitur:

```bash
apt install ffmpeg -y
```

Jalankan skrip untuk menginstal Node.js:

```bash
bash installnode.sh
```

Install Python 3.10 venv:

```bash
apt install python3.10-venv
```

Buat dan aktifkan virtual environment:

```bash
python3 -m venv venv && source venv/bin/activate
```

Install semua dependensi yang dibutuhkan oleh userbot:

```bash
pip3 install -r requirements.txt
```

## Langkah 4: Konfigurasi
Salin file konfigurasi contoh ke file `.env` dan buka untuk mengedit:

```bash
cp sample.env .env && nano .env
```

Lakukan perubahan yang diperlukan pada file `.env` sesuai dengan pengaturan bot kamu.

## Langkah 5: Menjalankan Userbot
Jalankan userbot menggunakan `screen` untuk memastikan proses tetap berjalan meskipun kamu logout:

```bash
screen -S ubotprem
python3 -m PyroUbot
```

## Langkah 6: Menghidupkan Ubot Jika Terhenti
Jika userbot mati dan perlu dihidupkan kembali, ikuti langkah-langkah berikut:

1. Masuk ke direktori `serpabot`:

    ```bash
    cd serpabot
    ```

2. Aktifkan virtual environment:

    ```bash
    python3 -m venv venv && source venv/bin/activate
    ```

3. Jalankan kembali userbot menggunakan `screen`:

    ```bash
    screen -S ubotprem
    python3 -m PyroUbot
    ```

Dengan mengikuti langkah-langkah ini, Userbot akan berjalan dengan lancar di server kamu.
