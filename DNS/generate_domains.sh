#!/bin/bash

# File to store the domain list
OUTPUT_FILE="domains.txt"

# Number of domains to generate
NUM_REAL=5000
NUM_RANDOM=5000

# Add real domains (use a curated list or fetch from a trusted source)
REAL_DOMAINS=(
  "example.com"
  "google.com"
  "facebook.com"
  "twitter.com"
  "linkedin.com"
  "amazon.com"
  "github.com"
  "wikipedia.org"
  "youtube.com"
  "microsoft.com"
)

# Write real domains with query type
for i in $(seq 1 $NUM_REAL); do
  echo "${REAL_DOMAINS[$((RANDOM % ${#REAL_DOMAINS[@]}))]} A IN" >> $OUTPUT_FILE
done

# Generate random domains with query type
for i in $(seq 1 $NUM_RANDOM); do
  echo "random${RANDOM}.test A IN" >> $OUTPUT_FILE
done

echo "Domain list created: $OUTPUT_FILE"
