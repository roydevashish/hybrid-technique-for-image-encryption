# 🔐 Hybrid Technique for Image Encryption

**A robust hybrid image encryption framework** combining symmetric and asymmetric cryptography to secure image data.

---

## 📖 Table of Contents

- [📌 Overview](#-overview)
  - [🔐 How It Works](#-how-it-works)
- [❗️ Prerequisites](#️-prerequisites)
- [⚙️ Getting Started](#️-getting-started)
  - [📥 Clone and Install](#-1-clone-and-install)
  - [🔐 Setup Environment Variables](#-2-setup-environment-variables)
  - [🏞️ Setup Images to Encrypt](#-3-setup-images-to-encrypt)
  - [🧪 Run the Project](#-4-run-the-project)
- [📁 Project Directory Structure](#-project-directory-structure)
  - [🗂️ File Structure](#️-file-structure)
  - [🔄 Root-Level Files](#-root-level-files)
  - [📁 `dataset/`](#-dataset)
  - [📁 `output/`](#-output)
  - [📁 `src/app/` — Core Logic](#-srcapp--core-logic)
  - [📁 `src/analysis/` — Analysis Logic](#-srcanalysis--analysis-logic)
- [📝 License](#-license)
- [🙋‍♂️ Maintainer](#-maintainer)

---

## 📌 Overview

This project implements a **hybrid image encryption framework** that sequentially applies two layers of encryption—**asymmetric (ECC)** followed by **symmetric (ChaCha20)**—to provide enhanced security for digital images.

Unlike traditional hybrid encryption schemes where the symmetric key is encrypted by an asymmetric algorithm, **this approach directly encrypts the image itself with both ECC and ChaCha20 in a cascaded fashion.** This adds redundancy, complexity, and resilience against cryptographic attacks.

### 🔐 How It Works

1. An input image is first encrypted using **Elliptic Curve Cryptography (ECC)**—a modern public-key encryption algorithm known for its strength and compact key sizes.
2. The ECC-encrypted image is then passed through the **ChaCha20** stream cipher for a second layer of symmetric encryption.
3. The resulting doubly encrypted image is stored, ensuring that compromising a single encryption layer does not expose the original image.
4. During decryption, the image undergoes **ChaCha20 decryption first**, followed by **ECC decryption**, to recover the original image.

This dual-layer strategy makes the system suitable for use cases requiring strong confidentiality guarantees—such as **secure image storage, transmission over untrusted networks, or cryptographic research**.

---

## ❗️ Prerequisites
- [Git](https://git-scm.com/downloads)
- [Python 3.12+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) - Python package and project manager

---

## ⚙️ Getting Started

### 1. 📥 Clone and Install

```bash
git clone https://github.com/roydevashish/hybrid‑technique‑for‑image‑encryption.git

cd hybrid‑technique‑for‑image‑encryption

uv sync
```

### 2. 🔐 Setup Environment Variables

Create a `.env` file in the root directory with the following:

```env
IMG_ORIGINAL=dataset
IMG_ENCRYPTED=output/encrypted
IMG_DECRYPTED=output/decrypted
ANALYSIS_DIR=output/analysis

CHACHA20_KEY=YOUR_CHACHA20_KEY_64_HEX_CHARACTER
CHACHA20_NONCE=YOUR_CHACHA20_NONCE_16_HEX_CHARACTER
ECC_PRIVATE_KEY=YOUR_ECC_PRIVATE_KEY_16_HEX_CHARACTER
```

### 3. 🏞️ Setup images to encrypt

Copy the original images that to be encrypted to the `/dataset` folder.

### 4. 🧪 Run the Project

```bash
uv run main.py
```

It will encrypt all the images at the `/dataset` folder and save the encrypted images at `/output/encrypted` folder, and decrypt all the encrypted images and save it to `/output/decrypted` folder.

---

## 📁 Project Directory Structure

### 🗂️ File Structure

```text
root
|-- dataset (Original images to be encrypted)
|   |-- sample.png
|
|-- output
|   |-- analysis (Analysis results/reports)
|   |   |-- entropy.csv (Entropy Analysis)
|   |
|   |-- decrypted (Decrypted images)
|   |   |-- sample.png 
|   |
|   |-- encrypted (Encrypted images)
|       |-- sample.png
|
|-- src
|   |-- analysys (Analysis logic)
|   |   |-- __init__.py
|   |   |-- entropy.py
|   |   |-- main.py
|   |
|   |-- app (Core logic)
|       |-- __init__.py
|       |-- chacha20.py
|       |-- ecc.py
|       |-- equation.py
|       |-- hybrid.py
|       |-- image.py
|       |-- main.py
|       |-- matrix.py
|       |-- padding.py
|
|-- .env.sample (Sample file for .env)
|-- .gitignore
|-- .python-version
|-- main.py (entry point)
|-- pyproject.toml
|-- README.md
|-- uv.lock
```

### 🔄 Root-Level Files

- **`main.py`** — 🚀 Entry point of the project. Runs the hybrid encryption and decryption pipeline.
- **`README.md`** — 📄 Documentation for setting up and understanding the project.
- **`.env.sample`** — ⚙️ Sample environment file defining secrets and path variables.
- **`.gitignore`** — 🚫 Specifies files and folders to ignore in version control.
- **`.python-version`** — 🐍 Python version specifier (used by tools like `pyenv`).
- **`pyproject.toml`** — 📦 Project metadata and dependency definitions.
- **`uv.lock`** — 🔒 Lockfile containing pinned dependency versions for reproducibility.

### 📁 `dataset/`

- Contains original **input images** to be encrypted.
- Example:
  - `sample.png` — raw/original image used for encryption.

### 📁 `output/`

- Stores all **result** related to project.
  - **`output/analysis/`** — 📊 Contains analysis results/reports.
  - **`output/encrypted/`** — 💾 Contains images after encryption.
  - **`output/decrypted/`** — 🔓 Contains images that were decrypted (should match originals).

### 📁 `src/app/` — Core Logic

| File             | Description |
|------------------|-------------|
| `__init__.py`     | Initializes the Python module. |
| `chacha20.py`     | Symmetric encryption via ChaCha20 stream cipher. |
| `ecc.py`          | Asymmetric encryption via ECC (Elliptic Curve Cryptography).|
| `equation.py`     | Solves quadratic equations used in calculation of dimensions of encrypted image. |
| `hybrid.py`       | Core pipeline combining ECC + ChaCha20 (hybrid encryption/decryption). |
| `image.py`        | Converts image to matrix and matrix back to image. |
| `main.py`         | Coordinates encryption/decryption of all images at `/dataset` folder. |
| `matrix.py`       | Converts matrix to string and string back to matrix. |
| `padding.py`      | Applies/removes padding to/from string with image metadata (height and width). |

### 📁 `src/analysis/` — Analysis Logic

| File             | Description |
|------------------|-------------|
| `__init__.py`     | Initializes the Python module. |
| `entropy.py`     | Calculate entropy of input, encrypted and decrypted images and write it to `output/analysis/entropy.csv` file. |
| `main.py`         | Coordinates all analysis. |

---

## 📝 License
No license specified as of now.

---

## 🙋‍♂️ Maintainer
GitHub: [@roydevashish](https://github.com/roydevashish)
