def extract_digits(input: str) -> list[str]:
    return [c for c in input if c.isdigit()]

def calc_total_sum(input: str) -> int:
    sum = 0
    for line in input.splitlines():
        digits = extract_digits(line)
        calibration_value = digits[0] + digits[-1]
        sum += int(calibration_value)
    return sum
