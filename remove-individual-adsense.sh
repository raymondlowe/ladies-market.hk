#!/bin/bash

# Script to remove individual AdSense units while preserving AutoAds
# Only removes individual ad units, not the main AutoAds script

echo "Removing individual AdSense units from HTML files..."

files=(
    "bird-market.html"
    "history-of-ladies-market.html"
    "how-to-get-there.html"
    "how-to-get-to-ladies-market-from-causeway-bay.html"
    "how-to-get-to-ladies-market-from-mongkok-mtr-station.html"
    "how-to-get-to-ladies-market-from-nathan-road.html"
    "how-to-get-to-ladies-market-from-tsim-sha-tsui.html"
    "jardine-s-crescent.html"
    "nearby-attractions.html"
    "nearby-hotels.html"
    "opening-hours-a.html"
    "opening-hours-old.html"
    "shopping.html"
    "stalls.html"
    "things-to-buy.html"
    "things-to-do.html"
    "where-to-eat.html"
)

for file in "${files[@]}"; do
    echo "Processing $file..."
    
    # Remove the adsense div block with class="adsense" and its contents
    sed -i '/<div class="adsense">/,/<\/div>/d' "$file"
    
    # Remove any standalone adsbygoogle script tags
    sed -i '/script.*adsbygoogle\.js.*<\/script>/d' "$file"
    
    # Remove any standalone ins class="adsbygoogle" tags
    sed -i '/<ins class="adsbygoogle"/,/<\/ins>/d' "$file"
    
    # Remove any standalone adsbygoogle push scripts
    sed -i '/((adsbygoogle.*push/d' "$file"
    
    echo "Completed $file"
done

echo "Individual AdSense units removal completed!"
echo "AutoAds script preserved in all files."