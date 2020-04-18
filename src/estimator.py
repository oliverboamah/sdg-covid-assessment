def estimator(data):
    output_data = {
        'data': data,
        'impact': get_estimate_data(input_data=data, is_severe_impact=False),
        'severeImpact': get_estimate_data(input_data=data, is_severe_impact=True)
    }
    return output_data


def get_estimate_data(input_data, is_severe_impact):
    scalar = 50 if is_severe_impact else 10

    reported_cases = int(input_data['reportedCases'])
    total_hospital_beds = int(input_data['totalHospitalBeds'])

    currently_infected = reported_cases * scalar
    infections_by_requested_time = currently_infected * 1024
    severe_cases_by_requested_time = infections_by_requested_time * 0.15
    hospital_beds_by_requested_time = (0.35 * total_hospital_beds) - severe_cases_by_requested_time
    cases_for_icu_by_requested_time = infections_by_requested_time * 0.05
    cases_for_ventilators_by_requested_time = infections_by_requested_time * 0.02
    dollars_in_flight = (infections_by_requested_time * 0.65) * 1.5 * 30

    output_data = {
        'currentlyInfected': currently_infected,
        'infectionsByRequestedTime': infections_by_requested_time,
        'severeCasesByRequestedTime': severe_cases_by_requested_time,
        'hospitalBedsByRequestedTime': hospital_beds_by_requested_time,
        'casesForICUByRequestedTime': cases_for_icu_by_requested_time,
        'casesForVentilatorsByRequestedTime': cases_for_ventilators_by_requested_time,
        'dollarsInFlight': dollars_in_flight
    }

    return output_data
