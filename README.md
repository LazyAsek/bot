# 🔎 OLX Offer Tracker

**An experimental web scraping and automation project built with Python.**

OLX Offer Tracker is a project designed to automate searching and monitoring listings on OLX.pl.

The main idea was to create a tool capable of scanning selected categories, extracting listing URLs, detecting newly published offers and eventually finding interesting deals before other buyers.

The project started as an experiment with web scraping and browser automation, but quickly evolved into a bigger idea involving automated deal discovery.

## ⚙️ Features

### Currently Implemented

- **Automated browsing** – Control a Chromium browser using Playwright.
- **OLX scraping** – Extract listing information from dynamically loaded OLX pages.
- **Sorting options** – Search listings by relevance, newest, cheapest or most expensive.
- **Dynamic filter extraction** – Retrieve available category filters and their options directly from OLX.
- **Listing URL extraction** – Collect and normalize links from search results.
- **Duplicate detection** – Compare collected links against previously saved listings.
- **New listing detection** – Separate newly discovered offers from previously stored ones.
- **Category-based monitoring** – Maintain separate listing files for different search topics.

### Planned Features

- Telegram notifications for newly discovered listings.
- SQLite database for storing listing IDs and historical data.
- Price comparison with BrickLink for LEGO listings.
- Automatic discount calculations.
- Listing previews with images and prices.
- Support for additional marketplaces such as Vinted, Allegro and eBay.
- 24/7 operation on a VPS or Raspberry Pi.

## 🛠️ Built With

- **Python** – Main programming language.
- **Playwright** – Browser automation and dynamic website interaction.
- **BeautifulSoup4** – HTML parsing and data extraction.
- **Chromium** – Browser engine controlled by Playwright.

## 📂 Project Structure

```text
bot-master/
├── plan/
│   ├── plan.docx
│   └── olx_map.docx
│
└── script/
    ├── data/
    │   ├── olx_links_iphone.txt
    │   ├── olx_links_kia.txt
    │   ├── olx_links_lego.txt
    │   ├── olx_links_oddam.txt
    │   └── olx_links_rower.txt
    │
    ├── main.py
    ├── olxHandler.py
    ├── linkMenager.py
    ├── openSite.py
    └── test.py
```

## 🚀 Getting Started

### Requirements

- Python 3.10+
- Chromium browser support through Playwright.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/LazyAsek/bot-master.git
   ```

2. Navigate to the project directory:

   ```bash
   cd bot-master
   ```

3. Install dependencies:

   ```bash
   pip install playwright beautifulsoup4
   ```

4. Install Playwright browsers:

   ```bash
   playwright install chromium
   ```

**Note:** The repository contains experimental modules and scripts. The main entry point and some module integrations still require adjustments before the project can be run as a complete application.

## 🧠 How It Works

The project is divided into several modules:

| Module | Responsibility |
|---|---|
| `openSite.py` | Browser automation, page loading and HTML parsing |
| `olxHandler.py` | OLX search handling, sorting, filters and link extraction |
| `linkMenager.py` | Listing storage and new/old offer comparison |
| `main.py` | Initial application entry point |
| `test.py` | Experimental scripts and functionality testing |

The general workflow:

1. Open OLX using an automated Chromium browser.
2. Search for a selected keyword.
3. Load dynamically generated listing results.
4. Extract listing URLs.
5. Compare them with previously collected links.
6. Identify newly discovered listings.
7. Save the collected data locally.

## 📈 Future Vision

The long-term goal was to turn this project into an automated deal-finding system.

LEGO was selected as the initial niche, with the idea of comparing second-hand listing prices against reference prices from BrickLink.

Eventually, the system could monitor multiple marketplaces and product categories, automatically identify attractive offers and send notifications whenever a potential deal appears.

## 📚 What I Learned

This project helped me explore several areas of software development:

- Web scraping and HTML parsing.
- Browser automation with Playwright.
- Working with dynamically loaded websites.
- CSS selectors and DOM manipulation.
- Object-oriented programming in Python.
- Data collection and duplicate detection.
- Separating application logic into independent modules.
- Planning and designing a larger automation system.

## ❤️ A Personal Note

This project represents an important step in my programming journey.

After experimenting with Java and game development in Slime Farm, I wanted to build something more practical – a tool that could interact with real websites and automate repetitive tasks.

What started as a simple OLX scraper turned into an idea for a much larger system.

Not every planned feature made it into the final implementation, but the project gave me valuable experience with Python, web automation and software architecture.

Looking back, it was one of the projects that pushed me towards more advanced programming concepts.

---

**Created by [LazyAsek](https://github.com/LazyAsek)**

*Built with Python, curiosity and a lot of experimentation.* 🔎

<img width="640" height="640" alt="1464342455-typing-cat-gif" src="https://github.com/user-attachments/assets/04570cbb-aff4-4b5d-9bc9-c62b6340d821" />
