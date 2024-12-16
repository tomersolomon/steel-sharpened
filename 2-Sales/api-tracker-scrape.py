import csv
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://apitracker.io/trending")

        with open('api-tracker-pull', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Company Name', 'Full URL', 'API Reference URL'])

            # Get all links at once
            links = await page.eval_on_selector_all(
                'a.hover\\:no-underline',
                'elements => elements.map(el => ({ href: el.href, companyName: el.href.split("/").pop() }))'
            )

            for link_data in links:
                company_name = link_data['companyName']
                full_url = link_data['href']

                # Navigate to the company page and extract API Reference URL
                try:
                    await page.goto(full_url)
                    await page.wait_for_selector('a:has-text("API Reference") >> visible=true', timeout=5000)
                    api_reference_link = await page.query_selector('a:has-text("API Reference")')

                    if api_reference_link:
                        api_reference_url = await api_reference_link.get_attribute("href")
                        print(f"Found API Reference for {company_name}: {api_reference_url}")
                    else:
                        api_reference_url = "Not Found"
                        print(f"API Reference not found for {company_name}.")

                except Exception as e:
                    print(f"Error processing {full_url}: {e}")
                    api_reference_url = "Error"

                # Go back and wait for navigation
                await page.go_back()
                await page.wait_for_url("https://apitracker.io/trending")

                writer.writerow([company_name, full_url, api_reference_url])

        await browser.close()

asyncio.run(main())