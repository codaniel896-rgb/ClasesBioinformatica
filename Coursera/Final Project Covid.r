# This lab requires 'httr' and 'rvest'packages, which are already pre-loaded into this lab environment.
# However, if you are working on your local RStudio, please uncomment the below codes and install the packages.

#install.packages("httr")
#install.packages("rvest")

library(httr)
library(rvest)


    
  # Our target COVID-19 wiki page URL is: https://en.wikipedia.org/w/index.php?title=Template:COVID-19_testing_by_country  
  # Which has two parts: 
    # 1) base URL `https://en.wikipedia.org/w/index.php  
    # 2) URL parameter: `title=Template:COVID-19_testing_by_country`, seperated by question mark ?
    
  # Wiki page base
  wiki_base_url <- "https://en.wikipedia.org/w/index.php"
  # You will need to create a List which has an element called `title` to specify which page you want to get from Wiki
  # in our case, it will be `Template:COVID-19_testing_by_country`
 
  # - Use the `GET` function in httr library with a `url` argument and a `query` arugment to get a HTTP response
    
  # Use the `return` function to return the response


library(httr)

get_wiki_covid19_page <- function() {

  # Wiki page base URL
  wiki_base_url <- "https://en.wikipedia.org/w/index.php"

  # Create a list of query parameters
  query_params <- list(
    title = "Template:COVID-19_testing_by_country"
  )

  # Send the HTTP GET request
  response <- GET(
    url = wiki_base_url,
    query = query_params
  )

  # Return the HTTP response
  return(response)
}
# Get the HTTP response
response <- get_wiki_covid19_page()

# Display the HTTP status code
status_code(response)

# Display the first 500 characters of the returned HTML
page_html <- content(response, as = "text", encoding = "UTF-8")
cat(substr(page_html, 1, 500))

# Read the exported CSV into a new data frame
covid_data_from_csv <- read.csv("covid19_data.csv")

# Select rows 5 to 10 and the requested columns
covid_subset <- covid_data_from_csv[
  5:10,
  c("country", "confirmed")
]

# Display the subset
print(covid_subset)

# Call the function
response <- get_wiki_covid19_page()

# Call the get_wiki_covid19_page function and print the response
# Call the function to get the HTTP response
response <- get_wiki_covid19_page()

# Get the root html node from the http response in task 1 

# Read the table node and convert it into a data frame, and print the data frame for review

library(httr)
library(rvest)

# Get the HTTP response from Task 1
response <- get_wiki_covid19_page()

# Get the root HTML node
html_node <- content(response, as = "text", encoding = "UTF-8") |>
  read_html()


# Get the table node from the root html node


# Get all table nodes
table_node <- html_nodes(html_node, "table")



# Extract the second table and convert it into a data frame
covid_table <- html_table(table_node[2], fill = TRUE) |>
  as.data.frame()

# View the resulting data frame
head(covid_table)

# Print the summary of the data frame
# Get a summary of the data frame
summary(covid_table)
str(covid_table)
dim(covid_table)
head(covid_table)

library(dplyr)

preprocess_covid_data <- function(df) {
  df <- df %>%
    # Remove irrelevant columns (adjust indices as needed)
    select(-c(1, 3)) %>%

    # Rename columns
    rename(
      Country = 1,
      Tested = 2,
      Confirmed = 3,
      Deaths = 4,
      Tests_per_million = 5
    ) %>%

    # Convert numeric columns
    mutate(
      Tested = as.numeric(gsub(",", "", Tested)),
      Confirmed = as.numeric(gsub(",", "", Confirmed)),
      Deaths = as.numeric(gsub(",", "", Deaths)),
      Tests_per_million = as.numeric(gsub(",", "", Tests_per_million))
    )

  return(df)
}

# Apply preprocessing
covid_data <- preprocess_covid_data(covid_table)

# Review the cleaned data
summary(covid_data)
str(covid_data)

reprocess_covid_data_frame <- function(data_frame) {

  # Remove the World row
  data_frame <- data_frame[
    data_frame$Country.or.region != "World", ]

  # Remove the last row, if present
  data_frame <- data_frame[1:min(172, nrow(data_frame)), ]

  # Remove unnecessary columns
  data_frame$Ref. <- NULL
  data_frame$Units.b. <- NULL

  # Rename columns
  names(data_frame) <- c(
    "country",
    "date",
    "tested",
    "confirmed",
    "confirmed.tested.ratio",
    "tested.population.ratio",
    "confirmed.population.ratio"
  )

  # Convert column data types
  data_frame$country <- as.factor(data_frame$country)
  data_frame$date <- as.factor(data_frame$date)

  numeric_columns <- c(
    "tested",
    "confirmed",
    "confirmed.tested.ratio",
    "tested.population.ratio",
    "confirmed.population.ratio"
  )

  data_frame[numeric_columns] <- lapply(
    data_frame[numeric_columns],
    function(x) as.numeric(gsub(",", "", x))
  )

  return(data_frame)
}

# Apply the preprocessing function
covid_data <- reprocess_covid_data_frame(covid_table)

# Inspect the cleaned data
summary(covid_data)
str(covid_data)

preprocess_covid_data_frame <- function(data_frame) {

  # Remove the World row
  data_frame <- data_frame[
    data_frame$Country.or.region != "World", ]

  # Remove the last row, if present
  data_frame <- data_frame[1:min(172, nrow(data_frame)), ]

  # Remove unnecessary columns
  data_frame$Ref. <- NULL
  data_frame$Units.b. <- NULL

  # Rename columns
  names(data_frame) <- c(
    "country",
    "date",
    "tested",
    "confirmed",
    "confirmed.tested.ratio",
    "tested.population.ratio",
    "confirmed.population.ratio"
  )

  # Convert column data types
  data_frame$country <- as.factor(data_frame$country)
  data_frame$date <- as.factor(data_frame$date)

  numeric_columns <- c(
    "tested",
    "confirmed",
    "confirmed.tested.ratio",
    "tested.population.ratio",
    "confirmed.population.ratio"
  )

  data_frame[numeric_columns] <- lapply(
    data_frame[numeric_columns],
    function(x) as.numeric(gsub(",", "", x))
  )

  return(data_frame)
}

# Apply the preprocessing function
covid_data <- reprocess_covid_data_frame(covid_table)

# Inspect the cleaned data
summary(covid_data)
str(covid_data)

# call `preprocess_covid_data_frame` function and assign it to a new data frame
covid_data <- preprocess_covid_data_frame(covid_table)


# Print the summary of the processed data frame again
summary(covid_data)


# Export the data frame to a csv file
write.csv(
  covid_data,
  file = "covid19_data.csv",
  row.names = FALSE
)

# Get working directory
wd <- getwd()
# Get exported 
file_path <- paste(wd, sep="", "/covid.csv")
# File path
print(file_path)
file.exists(file_path)

## Download a sample csv file
# covid_csv_file <- download.file("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-RP0101EN-Coursera/v2/dataset/covid.csv", destfile="covid.csv")
# covid_data_frame_csv <- read.csv("covid.csv", header=TRUE, sep=",")

# Read covid_data_frame_csv from the csv file

# Get the 5th to 10th rows, with two "country" "confirmed" columns
# Select rows 5 to 10 and columns country and confirmed
covid_subset <- covid_data[5:10, c("country", "confirmed")]

# Display the subset
covid_subset

# Get the total confirmed cases worldwide

# Get the total tested cases worldwide

# Get the positive ratio (confirmed / tested)

# Calculate worldwide totals
total_confirmed <- sum(covid_data$confirmed, na.rm = TRUE)
total_tested <- sum(covid_data$tested, na.rm = TRUE)

# Calculate the worldwide positive ratio
positive_ratio <- total_confirmed / total_tested

# Display the results
total_confirmed
total_tested
positive_ratio

# Display as a percentage
positive_percentage <- positive_ratio * 100
positive_percentage

# Get the `country` column

# Check its class (should be character)

# Sort the countries AtoZ

# Sort the countries ZtoA

# Print the sorted ZtoA list

# Get the sorted list of countries
country_list <- sort(unique(as.character(covid_data$country)))

# Display the list
country_list

length(country_list)

# Get the country column
country_list <- as.character(covid_data$country)

# Check its class
class(country_list)

# Sort the countries A to Z
country_list_AtoZ <- sort(country_list)

# Sort the countries Z to A
country_list_ZtoA <- sort(country_list, decreasing = TRUE)

# Print the sorted Z to A list
country_list_ZtoA

# Use a regular expression `United.+` to find matches

# Print the matched country names

# Find countries starting with "United"
united_countries <- grep(
  "^United",
  country_list,
  value = TRUE
)

# Print the matching countries
united_countries

# Find country names matching the regular expression "United.+"
united_countries <- grep(
  "United.+",
  country_list,
  value = TRUE
)

# Print the matched country names
united_countries

# Select a subset (should be only one row) of data frame based on a selected country name and columns


# Select a subset (should be only one row) of data frame based on a selected country name and columns


# Select two countries
selected_countries <- covid_data[
  covid_data$country %in% c("United States", "United Kingdom"),
  c("country", "confirmed", "confirmed.population.ratio")
]

# Display the comparison
selected_countries

# Use if-else statement
# if (check which confirmed.population value is greater) {
#    print()
# } else {
#    print()
# }

# Compare confirmed cases to population ratio
if (selected_countries$confirmed.population.ratio[1] >
    selected_countries$confirmed.population.ratio[2]) {

  print(paste(
    selected_countries$country[1],
    "has the larger confirmed cases to population ratio."
  ))

} else {

  print(paste(
    selected_countries$country[2],
    "has the larger confirmed cases to population ratio."
  ))
}

selected_countries[
  which.max(selected_countries$confirmed.population.ratio),
  c("country", "confirmed.population.ratio")
]

# Get a subset of any countries with `confirmed.population.ratio` less than the threshold

# Set the threshold to 1%
threshold <- 0.01

# Get countries with confirmed population ratio below 1%
low_ratio_countries <- covid_data[
  covid_data$confirmed.population.ratio < threshold,
  c("country", "confirmed.population.ratio")
]

# Display the results
low_ratio_countries


