#	
(        std::cout << "--- TRINITY AUDIT: INTEGRITY VERIFIED ---" << std::endl;
        for (int i = 0; i < ledger.weather_data_size(); i++) {
            const auto& gate = ledger.weather_data(i);
            std::cout << "[ENTRY] Temp: " << gate.temperature() << " | Hash: " << gate.entry_hash() << std::endl;
        }
    }
    input.close();

    // 2. BRIDGE PHASE (Add new data)
    float t; std::cout << "Enter new Temperature: "; std::cin >> t;
    GeoWeatherGate* new_gate = ledger.add_weather_data();
    new_gate->set_temperature(t);
    new_gate->set_entry_hash(sha256(std::to_string(t)));

    std::fstream output(filename, std::ios::out | std::ios::binary | std::ios::trunc);
    ledger.SerializeToOstream(&output);
    std::cout << "--- TRINITY BRIDGE: TRUTH COMMITTED ---" << std::endl;

    return 0;
}
