#!/bin/bash

# Generate random data (16 bytes)
random_data=$(openssl rand -hex 16 | tr -dc '[:alnum:]' | head -c 32)

echo "Original Random Data (Hex): $random_data"

# Split data into two parts (ensure even length)
data_length=${#random_data}
mid_point=$(( data_length / 2 ))

part1=${random_data:0:$mid_point}
part2=${random_data:$mid_point}

# Ensure both parts have the same number of characters (important for XOR)
if [[ ${#part1} -ne ${#part2} ]]; then
  # Pad the shorter part with zeros
  shorter_part=${#part1}
  longer_part=${#part2}
  padding_length=$((longer_part - shorter_part))
  if [[ $shorter_part -eq $mid_point ]]; then
    part1+=$(printf "%0${padding_length}d" 0)
  else
    part2+=$(printf "%0${padding_length}d" 0)
  fi
fi

echo "Part 1: $part1"
echo "Part 2: $part2"

# Calculate parity using XOR (ensure 32-digit format without leading zeros)
parity=$(printf "%x" $(( 0x$part1 ^ 0x$part2 )))

echo "Parity: $parity"

# Simulate data loss
lost_part=$part1
remaining_part=$part2

# Recover lost part using XOR
recovered_part=$(printf "%x" $(( 0x$parity ^ 0x$remaining_part )))

echo "Recovered Part: $recovered_part"

# Combine recovered and remaining parts
original_data="$recovered_part$remaining_part"

# Remove leading zeros from recovered data (optional)
original_data=${original_data#0}

echo "Recovered Random Data (Hex): $original_data"

