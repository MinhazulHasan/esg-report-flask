financial_fields = [
    {
        "data_field": "Revenue",
        "description": "Revenue for the most recent fiscal year avaialble (indicate year). Explicit indication of currency",
        "query": "Provide the annual Revenue of '{company_name}' for all available years.",
        "expected_value": "Millions of currency",
    },
    {
        "data_field": "Enterprise Value",
        "description": "EV for the most recent fiscal year avaialble (indicate year). Explicit indication of currency",
        "query": "Provide the annual Enterprise Value of '{company_name}' for all available years.",
        "expected_value": "Millions of currency",
    },
    {
        "data_field": "MarketCap",
        "description": "Market cap for the most recent fiscal year avaialble (indicate year). Explicit indication of currency",
        "query": "Provide the annual MarketCap of '{company_name}' for all available years.",
        "expected_value": "Millions of currency",
    }
]



gsg_fields = [
    {
        "data_field": "Most Recent GHG S1",
        "description": "reported and most recent GHG emissions for scope 1 for the company",
        "query": "Provide the most recent GHG emissions for scope 1 for `{company_name}` for all available years.",
        "expected_value": "tCO2e",
    },
    {
        "data_field": "Most Recent GHG S2",
        "description": "reported and most recent GHG emissions for scope 2 for the company",
        "query": "Provide the most recent GHG emissions for scope 2 for `{company_name}` for all available years.",
        "expected_value": "tCO2e",
    },
    {
        "data_field": "Most Recent GHG S3",
        "description": "reported or estimated and most recent GHG emissions for scope 3 for the company. If available a breakdown for any of the 15 subcategories",
        "query": "Provide the most recent GHG emissions for scope 3 for `{company_name}` for all available years.",
        "expected_value": "tCO2e",
    }
]



boolean_fields = [
    {
        "data_field": "Target NetZero",
        "description": "Indicates whether the target aims for 'net zero' emissions, as defined by the company",
        "query": "Does '{company_name}' have a target for net zero emissions?",
        "expected_value": "Yes/No",
    },
    {
        "data_field": "SBTi Target Approved",
        "description": "the company has one or more active carbon emissions reduction target/s approved by the Science Based Targets initiative (SBTi)",
        "query": "Does '{company_name}' have SBTi Target Approved?",
        "expected_value": "Yes/No",
    },
    {
        "data_field": "Conventional Weapons",
        "description": "Companies that have an industry tie to conventional weapons",
        "query": "Does `{company_name}` have an industry tie to conventional weapons?",
        "expected_value": "Yes/No/Not disclosed",
    },
    {
        "data_field": "Controversial Weapons Exposure",
        "description": "whether Company has an industry tie to landmines, cluster munitions, chemical weapons or biological weapons. Note: industry tie includes ownership, manufacture or investment. Landmines do not include related safety products",
        "query": "Does `{company_name}` have Controversial Weapons Exposure?",
        "expected_value": "Yes/No/Not disclosed",
    },
    {
        "data_field": "Countries Social Violations",
        "description": "whether Countries alleged to be involved in human rights violations and abuses can be subject to EU sanctions. Data source: European External Action Service",
        "query": "Does `{company_name}` have Countries Social Violations?",
        "expected_value": "Yes/No/Not disclosed",
    },
    {
        "data_field": "Deforestation Policies",
        "description": "whether companies has deforestation policies",
        "query": "Does '{company_name}' have deforestation policies?",
        "expected_value": "Yes/No/Not disclosed",
    },
    {
        "data_field": "Emissions Reduction Policies",
        "description": "companies without carbon emission reduction initiatives. Linked to the set of points relating to emissions reduction targets. If not reported targets, fields above are blanks",
        "query": "Does '{company_name}' have emissions reduction policies?",
        "expected_value": "Yes/No/Not disclosed",
    },
    {
        "data_field": "Lack of anti-corruption and anti-bribery policies",
        "description": "Company has an anti-corruption and anti-bribery policy consistent with the United Nations Convention against Corruption",
        "query": "Does '{company_name}' have an anti-corruption and anti-bribery policy?",
        "expected_value": "Yes/No/Not disclosed",
    },
    {
        "data_field": "Lack of a supplier code of conduct",
        "description": "whether has a  supplier code of conduct.  Includes commitments to eradicate unsafe working conditions, precarious work, child labor and forced labor",
        "query": "Does '{company_name}' have a supplier code of conduct?",
        "expected_value": "Yes/No/Not disclosed",
    },
    {
        "data_field": "Human Rights Policies",
        "description": "Company has a human rights policy",
        "query": "Does '{company_name}' have a human rights policy?",
        "expected_value": "Yes/No/Not disclosed",
    },
    {
        "data_field": "Water Stress Exposure",
        "description": "whether Company discloses operations in areas of high water stress but lacks mater management policies",
        "query": "Does '{company_name}' involve in water stress exposure?",
        "expected_value": "Yes/No/Not disclosed",
    },
    {
        "data_field": "Extreme Water Stress",
        "description": "Company's operations are exposed to areas where the percentage of total water withdrawn is high or extremely high",
        "query": "Does '{company_name}' have operations in areas of extreme water stress?",
        "expected_value": "Yes/No/Not disclosed",
    },
    {
        "data_field": "Adult Entertainment",
        "description": "Companies with an industry tie to adult entertainment, including producer, distributor, retailer, and ownership categories",
        "query": "Does '{company_name}' have an industry tie to adult entertainment?",
        "expected_value": "True/False",
    },
    {
        "data_field": "Alcohol",
        "description": "Companies with an industry tie to alcohol, including producer, distributor, retailer, licensor, supplier, and ownership categories",
        "query": "Does '{company_name}' have an industry tie to alcohol?",
        "expected_value": "True/False",
    },
    {
        "data_field": "Gambling Activities",
        "description": "Companies that have an industry tie to gambling through the operation, support, licensing or ownership categories",
        "query": "Does '{company_name}' have gambling activities?",
        "expected_value": "True/False",
    },
    {
        "data_field": "Tobacco Producer",
        "description": "Companies that manufacture tobacco products, such as cigars, blunts, cigarettes, e-cigarettes, inhalers, beedis, kreteks, smokeless tobacco, snuff, snus, dissolvable and chewing tobacco. This also includes companies that grow or process raw tobacco leaves",
        "query": "Does '{company_name}' manufacture tobacco products?",
        "expected_value": "True/False",
    }
]



miscellaneous_fields = [
    {
        "data_field": "Scope",
        "description": "Scope combinations covered by the targets",
        "query": "What scope combinations are covered by the targets for {company_name}?",
        "expected_value": "S1 or S2 or S1+S2 or S1+S2+S3 or S3",
    },
    {
        "data_field": "Coverage_S1",
        "description": "The part of emissions covered in scope 1 for the target",
        "query": "What percentage of Scope 1 emissions does the target for {company_name} cover?",
        "expected_value": "percentage",
    },
    {
        "data_field": "Coverage_S2",
        "description": "The part of emissions covered in scope 2 for the target",
        "query": "What percentage of Scope 2 emissions does the target for {company_name} cover?",
        "expected_value": "percentage",
    },
    {
        "data_field": "Coverage_S3",
        "description": "The part of emissions covered in scope 3 for the target. This should be the coverage compared to the whole scope 3 emissions",
        "query": "What percentage of Scope 3 emissions does the target for {company_name} cover?",
        "expected_value": "percentage",
    },
    {
        "data_field": "Reduction ambition",
        "description": "The emission reduction that is set as an ambition in the target",
        "query": "What is the emission reduction ambition set in the target for {company_name}?",
        "expected_value": "percentage",
    },
    {
        "data_field": "Total Energy Consumption",
        "description": "Share of total energy consumption of investee companies from all energy sources",
        "query": "Total Energy Consumption for `{company_name}`",
        "expected_value": "GWh",
    },
    {
        "data_field": "Total Renewable Consumption",
        "description": "Share of non-renewable energy consumption of investee companies from non-renewable energy sources",
        "query": "Total Renewable Consumption for `{company_name}`",
        "expected_value": "GWh",
    },
    {
        "data_field": "Renewable Energy Production",
        "description": "Share of non-renewable energy production  of investee companies from non-renewable energy sources",
        "query": "Renewable Energy Production for `{company_name}`",
        "expected_value": "GWh",
    },
    {
        "data_field": "Emissions to Water",
        "description": "Tonnes of emissions to water : Total tons of pollutants released to surface waters as a result of companies' operations",
        "query": "Emissions to Water for `{company_name}`",
        "expected_value": "tonnes",
    },
    {
        "data_field": "Hazardous Waste",
        "description": "Tonnes of hazardous waste and radioactive waste generated by  companies",
        "query": "Hazardous Waste for `{company_name}`",
        "expected_value": "tonnes",
    },
    
    {
        "data_field": "GHG emissions Countries",
        "description": "Total Greenhouse Gas emissions in a country represented in terms of Tons CO2 equivalent. Source: EDGAR",
        "query": "Total GHG emissions for `{company_name}`",
        "expected_value": "tCO2e",
    },
    {
        "data_field": "Nuclear energy consumption",
        "description": "Energy consumption from nuclear power",
        "query": "What is the total energy consumption from nuclear power (in GWh) by `{company_name}`?",
        "expected_value": "GWh",
    },
    {
        "data_field": "Nuclear energy generation",
        "description": "power generation from nuclear sources",
        "query": "What is the contribution to nuclear energy generation of `{company_name}`?",
        "expected_value": "GWh",
    },
    {
        "data_field": "Thermal coal generation",
        "description": "Generation Output from thermal coal",
        "query": "What is the generation output from thermal coal for `{company_name}` (in GWh)?",
        "expected_value": "GWh",
    },
    {
        "data_field": "Tobacco Retailer Revenue",
        "description": "The  percent of revenue, or maximum estimated percent, a company has derived from retail sales of tobacco products",
        "query": "What is the percentage of revenue derived from retail sales of tobacco products by `{company_name}`?",
        "expected_value": "percentage",
    },
    {
        "data_field": "Tobacco Distributor Revenue",
        "description": "The  percent of revenue, or maximum estimated percent, a company has derived from distribution of tobacco products",
        "query": "What percentage of revenue from tobacco product Distribution is made by `{company_name}`?",
        "expected_value": "percentage",
    },
    {
        "data_field": "Tobacco Supplier Revenue",
        "description": "The recent-year percent of revenue, or maximum estimated percent, a company has derived from supplying products essential to the tobacco industry",
        "query": "What percentage of revenue derived from supplying products essential to the tobacco industry by `{company_name}`?",
        "expected_value": "percentage",
    },
    {
        "data_field": "Gender Pay Gap between female and male employees",
        "description": "The difference between the average gross hourly earnings of male and female employees as a percentage of male gross earnings. Note that reporting on this metric is inconsistent: some companies report on the absolute or uncontrolled pay gap while others control for compensable factors such as role or location",
        "query": "Gender Pay Gap between female and male employees for {company_name}",
        "expected_value": "numeric ratio",
    },
    {
        "data_field": "Board Gender Diversity",
        "description": "Average ratio of female to male board members in the companies",
        "query": "Average ratio of female to male board members in {company_name}",
        "expected_value": "percentage",
    }
]



data_fields = [
    {
        "data_field": "Financial Year",
        "description": "fiscal year of the most recent reported or estimated/GHG values. If available, it should be reported per each data point. As levels of disclosure may be different",
        "expected_value": "numeric/year",
    },
    {
        "data_field": "Sector Classification",
        "description": "NACE or GICS classification at the most granular level",
        "expected_value": "Code and sector description",
    },
    {
        "data_field": "Target Description",
        "description": "Full description of the emission reduction targets. Should containt timeframe of the targets (years), ambition, scopes, target type and base year emissions",
        "expected_value": "Reduce 46% of  scope 1 and 2 emissions by year 2030 compared to 2019 baseline year. 10% renewable gas across its distribution networks by 2030 and achieve full  renewable gas conversion",
    },
    {
        "data_field": "Target type",
        "description": "Absolute or intensity based GHG emission reduction target",
        "expected_value": "Absolute: absolute emissions, intensity: GHG intensity of 7.37 normalized to revenue, other",
    },
    {
        "data_field": "Intensity metric",
        "description": "The metric on which the intensity-based GHG emission reduction target is based. All intensity metrics must be mapped to the 8 categories",
        "expected_value": "Revenue (tCO2e/revenue), Product, Cement, Oil, Steel, Aluminum, Power Generation, or Other",
    },
    {
        "data_field": "Base year",
        "description": "Base year of the target",
        "expected_value": "numeric/year",
    },
    {
        "data_field": "End year",
        "description": "End year of the target",
        "expected_value": "numeric/year",
    },
    {
        "data_field": "Start year",
        "description": "Year the target was announced. If not specified, it will be assumed the start year is equal to the base year",
        "expected_value": "numeric/year",
    },
    {
        "data_field": "Achieved reduction",
        "description": "Part of the reduction ambition of the target that is already achieved by the company",
        "expected_value": "Number between 0 and  < 1 or 0  to  < 100 --> 70%== 0.7",
    },
    {
        "data_field": "Fossils fuel exposure",
        "description": "whether the company is involved in any fossil fuels related activities: extraction, processing, storage and transportation of petroleum products, natural gas, and thermal and metallurgical coal",
        "expected_value": "Yes/No/Not disclosed",
    },
    {
        "data_field": "Negative Activities Biodiversity Areas",
        "description": "whether Company reports having operations in or near to biodiversity sensitive areas and has been implicated in controversies with severe or very severe adverse impact on the environment",
        "expected_value": "Yes/No/Not disclosed",
    },
    {
        "data_field": "Global Violations of UN principles",
        "description": "whether companies have been involved in violations of the UNGC principles or OECD Guidelines for Multinational enterprise, the UN Guiding principles",
        "expected_value": "Yes/No/Not disclosed. In case of yes: level of severity of the violations/controversies",
    },
    {
        "data_field": "Lack of processes and  mechanisms to monitor compliance with OECD Guidelines",
        "description": "whether the companies have in place policies to monitor compliance with or with grievance/ complaints handling mechanisms to address violations of the OECD Guidelines for Multinational Enterprises, the UN Guiding principles",
        "expected_value": "Yes/No/Not disclosed",
    },
    {
        "data_field": "GDPNominal",
        "description": "For sovereigns: nominal GDP of a country. Explicit indication of reported currency. Source: WDI, CIA",
        "expected_value": "",
    }
]
