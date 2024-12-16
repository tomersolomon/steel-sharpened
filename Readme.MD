# :nut_and_bolt:  Sharpend Steel: A Stainless Deep Dive :nut_and_bolt:

This project analyzes [Stainless](https://www.stainlessapi.com/), a company that automatically generates - and maintains - SDKs from OpenAPI YAML specifications. The goal is to better understand the product, market landscape, and propose preliminary S&M ideas through a hands-on and proof-of-concept approach. 

We've broken down the analysis into four segments: (1) Product, (2) Sales, (3) Marketing, and (4) Finance.

## :computer:  1. Product  :computer: 

The core of Stainless's business is SDK generation from OpenAPI YAML files. 

We've built an MVP to better understand and demonstrate this process (redirects to Vimeo video):

[![Watch the demo](1-Product/steel-gif.gif)](https://vimeo.com/1039740766)
|:--:|
| *Steel Product Demo (Vimeo)* |

We generate local SDK configurations by parsing a provided YAML, prompting for the desired SDK language (i.e. Python or Node), and then use Jinja templates to create language-specific SDKs which are then stored in the `1-Product/output-sdk` folder. This MVP helps us understand the underlying mechanics of products like [Stainless](https://www.stainlessapi.com/), [Speakeasy](https://www.speakeasy.com/), and [OpenAPI Generator](https://openapi-generator.tech/) on the open source side. 

**Key Features of the MVP:**

*   **SDK Generation:** Creates Python and Node.js SDKs from local OpenAPI YAML files.
*   **README Generation for each Language:** Automatically generates a `README.md` for each SDK, outlining the API and its endpoints.

Future MVP development steps include: auto-generating SDK endpoint tests, creating a Click-based CLI, containerizing with Docker, and implementing GitHub Actions for remote connectiviely and YAML-driven automation.

## :telephone_receiver: 2. Sales: Growth Engineering :telephone_receiver:

The objective here is to identify potential customers via an engineering-first approach. We've focused on three target groups:

1. **Public OpenAPI YAML's:** We used [https://api.apis.guru/](https://api.apis.guru/) - an API that aggreagates API's - to source publicly available OpenAPI YAML files and then wrote a script to parse contact information, documentation links, and the YAML files themselves. A proof of concept to shower a creative ways of driving growth via sourcing OpenAPI YAML files. 
2. **API Companies:** Next we leveraged the power of web scraping. We developed a Playwright-based web scraper to extract a list of API companies from [API-Tracker](https://apitracker.io/). This approach can be extended to platforms like the Postman Public API Network.
3. **API Platform Engineers:** We then targeted API platofrm engineers. We leveraged [Apollo](https://app.apollo.io/)'s database to identify US-based API platform engineers as a target audience. The Airtable link to the raw data is [here](https://airtable.com/invite/l?inviteId=invd0Bdkxy2kO2mpM&inviteToken=006ffec975303653a34df28a46e9ad45c1e2b3b25893625e048fecbfb26d63df&utm_medium=email&utm_source=product_team&utm_content=transactional-alerts).

Next steps include enhancing workflow efficiency by integrating data into [Attio](https://attio.com/) (CRM), using [Clay](https://www.clay.com/) for enrichment, developing a lead-scoring model, and running scaled outbound campaigns with tools like [Instantly](https://instantly.ai/).

## :mega: 3. Marketing: API Community and Content :mega:

We propose a three-pronged marketing strategy:

1. **Events:** A calendar of relevant industry events to participate in.

    ![3-Marketing/api-events_table.png](3-Marketing/api-events_table.png)

2. **Video/Webinar Content:** A schedule for creating and publishing video content (e.g., tutorials, demos, webinars).

 ![3-Marketing/video-schedule_table.png](3-Marketing/video-schedule_table.png)

3. **Blog Content:** A plan for  blog posts covering technical deep dives, use cases, and industry insights with a focus on customer testimonials.

    ![3-Marketing/blog-schedule_table.png](3-Marketing/blog-schedule_table.png)

Given the nature of the product, product-led and marketing-led will be key but the business can also uniquely target companies with public YAML files which provides a unique sales angle.

## :dollar: 4. Finance: Competitive Landscape and Pricing :dollar:

We performed a preliminary competitive analysis to understand the ecosystem and get a sense of pricing. We also began formulating a few [investor-esque questions](https://github.com/tomersolomon/steel-sharpened/blob/Main/4-Finance/investory-questions.MD) based on our current understanding of the business. See `comps_and_ecosystem.json` for our competitive analysis. A few observations:

*   **Speakeasy:** The notable "K-Nearest Neighbor" comp that also just recently raised venture funding from GV so will be a notable competitor. A few highlights are their Terraform offering for the infrastructure market and their local CLI which offers a more controlled SDK development experience. 

*   **Terraform Opportunity:** Terraform and cloud infrastructure market seems like a very attractice opportunity to enter as it's an underserviced segment that Stainless can capture with our YAML-driven platform.

*   **Partnerships** There are interesting potential partnership opportunities in documentation (depending on Stainless's build vs. buy strategy) as well as with CLI players like CircleCI and API management companies like Kong. 

Reach out at [@tomer_solomon](https://twitter.com/tomer_solomon) for any questions and thoughts!
