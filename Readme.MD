# :nut_and_bolt:  Sharpend Steel: A Stainless Deep Dive :nut_and_bolt:

This project analyzes [Stainless](https://www.stainlessapi.com/), a Series A company that generates SDKs from OpenAPI YAML specifications. The goal is to understand the product, business model and propose preliminary ideas through a hands-on and proof-of-concept approach. We've broken down the analysis into four segments: (1) Product, (2) Sales, (3) Marketing, and (4) Finance.

## :computer:  1. Product  :computer: 

The core of [Stainless](https://www.stainlessapi.com/)'s business is SDK generation from OpenAPI YAML files. We've built an MVP to understand and demonstrate this process:

<!-- <video width="640" height="360" controls>
  <source src="https://github.com/tomersolomon/steel-sharpened/blob/Main/1-Product/steel-sdk-demo-min.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video> -->

We generate SDK configurations by parsing a provided YAML, prompting for the desired SDK language, and then using Jinja templates to create language-specific SDKs. This MVP helps us understand the underlying mechanics of products like [Stainless](https://www.stainlessapi.com/), [Speakeasy](https://www.speakeasy.com/), and [OpenAPI Generator](https://openapi-generator.tech/).

**Key Features of the MVP:**

*   **SDK Generation:** Creates Python and Node.js SDKs from local OpenAPI YAML files.
*   **README Generation for each Language:** Automatically generates a `README.md` for each SDK, outlining the API and its endpoints.
*   **YAML File Inclusion:** Copies the input OpenAPI YAML file into the SDK directory to have for reference.

**Next Steps for MVP Product Development:**

1. **Endpoint Test Generation:** Automatically generate test cases for each API endpoint within the SDKs.
2. **CLI Interface with Click:** Build a user-friendly command-line interface for the SDK generator using the Click library.
3. **Dockerization:** Containerize the application with Docker for consistent performance across environments.
4. **Automated Github Updates:** Learn how to automated SDK updates using GitHub Apps and Actions, triggered by changes to the YAML file. Explore automated pushing to remote GitHub repositories.

## :telephone_receiver: 2. Sales: Growth Engineering :telephone_receiver:

The objective here is to identify potential customers via engineering-first approach. We've focused on three target groups:

1. **Public OpenAPI YAML Files:** We used [https://api.apis.guru/](https://api.apis.guru/) - an API that aggreagates API's - to source publicly available OpenAPI specifications, along with contact information, documentation links, and the YAML files themselves. A proof of concept to shower a creative ways of driving growth via sourcing OpenAPI YAML files. 
2. **API Companies:** Next we leveraged the power of web scraping. We developed a Playwright-based web scraper to extract a list of API companies from [API-Tracker](https://apitracker.io/). This approach can be extended to platforms like the Postman Public API Network.
3. **API Platform Engineers:** We then targeted People over Companies. We leveraged [Apollo](https://app.apollo.io/)'s database to identify US-based API platform engineers as a target audience. The Airtable link to the raw data is [here](https://airtable.com/appk7oNE7MdJbQN2J/tblw2YX2mHmcLsIjh/viwOl95O8Rz7IWXVe?blocks=hide).

This of course exludes plenty of other channels - namley targeting high growth AI & API first companies within the same investor ecosystem - but serves as a way to demonstrate creative and engineering-first approaches in growth. Future steps involve:

*   **CRM Integration:** Unifying the collected data into a CRM such as [Attio](https://attio.com/) system and leveraging [Clay](https://www.clay.com/) for data enrichment.
*   **Lead Scoring:** Developing a lead scoring model based on fit and relevance.
*   **Scaled Outbound Campaigns:** Creating targeted campaigns using tools like Instantly.

## :mega: 3. Marketing: API Community and Content :mega:

We propose a three-pronged marketing strategy:

1. **Events:** A calendar of relevant industry events to participate in.

    ![3-Marketing/api-events_table.png](3-Marketing/api-events_table.png)

2. **Video/Webinar Content:** A schedule for creating and publishing video content (e.g., tutorials, demos, webinars).

 ![3-Marketing/video-schedule_table.png](3-Marketing/video-schedule_table.png)

3. **Blog Content:** A plan for consistent blog posts covering technical deep dives, use cases, and industry insights.

    ![3-Marketing/blog-schedule_table.png](3-Marketing/blog-schedule_table.png)

Given the nature of the product, product-led and marketing-led will be key but the business can also uniquely target companies with public YAML files so focused sales will also be strategic. 

## :dollar: 4. Finance: Competitive Landscape and Pricing :dollar:

We performed a preliminary competitive analysis to understand the ecosystem, identify potential partners, and get a sense of pricing models. We also began formulating a few investor-related questions based on our current understanding of the business. See `comps_and_ecosystem.json` for our competitive analysis. A few observations

*   **Speakeasy:** The notable "K-Nearest Neighbor" comp. A few highlights are their Terraform offering for the infrastructure market and their local CLI which offers a more controlled SDK development experience. 

*   **Partnerships** Tre are interesting potential partnership opportunities in documentation (depending on Stainless's build vs. buy strategy), with CLI players like CircleCI, and API management companies like Kong, etc.

*   **Investor Questions:** We have compiled a list of investor questions in a separate document (`questions.md`) to further explore the financial aspects of Stainless's business.

## :scroll: Conclusion :scroll: 

This project provides a comprehensive analysis of Stainless' business, focusing on the core product alongside potential ideas for sales strategy, marketing, and marketing landscape. A starting point for anyone interested in learning more as well as understandign the intricacies of the API economy!