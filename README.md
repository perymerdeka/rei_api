# Rei API CLI Tools

tools to get product from rei.com

## Get Started

### From Source

make sure use virtual environment with this command

```sh
 python -m venv venv
```

```sh
 venv\Scripts\activate # on windows
```

```sh
 source venv/bin/activate # on mac or linux
```

```bash
pip install -r requirements.txt --no-cache-dir
```

```
cd src/
```

then run the script and type

```bash
python main.py --help

 Usage: main [OPTIONS] COMMAND [ARGS]...

╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                                                                                                                       │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.                                                                                                                │
│ --help                        Show this message and exit.                                                                                                                                                                     │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ scrape                               Menjalankan Scraping semua halaman pada satu situs berdasarkan kata kunci tertentu                                                                                                       │
│ spesific_scrape                      scraping situs berdasarkan kata kunci dan halaman tertentu                                                                                                                               │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

to get spesific scrape and scrape help usage type

```bash
python main.py scrape --help

 Usage: main scrape [OPTIONS] SEARCH_QUERY

 Menjalankan Scraping semua halaman pada satu situs berdasarkan kata kunci tertentu

╭─ Arguments ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    search_query      TEXT  [default: None] [required]                                                                                                                                                                       │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --filepath    --no-filepath      Digunakan untuk Menentukan lokasi generate laporan hasil scraping, (Jika Diisi) contoh ./data.csv [default: no-filepath]                                                                     │
│ --is-csv      --no-is-csv        generate hasil scraping menjadi CSV, jika Filepath diisi [default: no-is-csv]                                                                                                                │
│ --is-excel    --no-is-excel      generate hasil scraping menjadi file excel, (Jika Filepath diisi) [default: no-is-excel]                                                                                                     │
│ --is-json     --no-is-json       generate hasil scraping menjadi sebuah File JSON jika filepath diisi [default: no-is-json]                                                                                                   │
│ --help                           Show this message and exit.                                                                                                                                                                  │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

and for `spesific scrape` type

```bash
python main.py spesific_scrape  --help

 Usage: main spesific_scrape [OPTIONS] SEARCH_QUERY PAGE

 scraping situs berdasarkan kata kunci dan halaman tertentu

╭─ Arguments ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    search_query      TEXT     [default: None] [required]                                                                                                                                                                    │
│ *    page              INTEGER  [default: None] [required]                                                                                                                                                                    │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --filepath                     TEXT  Digunakan untuk Menentukan lokasi generate laporan hasil scraping, (Jika Diisi) contoh ./data.csv [default: None]                                                                        │
│ --is-csv      --no-is-csv            generate hasil scraping menjadi CSV, jika Filepath diisi [default: no-is-csv]                                                                                                            │
│ --is-excel    --no-is-excel          generate hasil scraping menjadi file excel, (Jika Filepath diisi) [default: no-is-excel]                                                                                                 │
│ --is-json     --no-is-json           generate hasil scraping menjadi sebuah File JSON jika filepath diisi [default: no-is-json]                                                                                               │
│ --help                               Show this message and exit.                                                                                                                                                              │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```


#### Example

to run scraper and scrape all product by keywords u can type

```bash
python main.py scrape Shoes
```

then for spesific scrape and then generate report

```bash
python main.py spesific_scrape shoes 2 --filepath="./data.xlsx" --is-excel
```

Thanks!, feel happy to report a bugs and issues if u found it
