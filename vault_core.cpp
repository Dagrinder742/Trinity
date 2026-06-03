#include <iostream>
#include <fstream>
#include <string>
#include <openssl/sha.h>
#include "trinity.pb.h"

// Helper to calculate SHA256
std::string sha256(const std::string str) {
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, str.c_str(), str.size());
    SHA256_Final(hash, &sha256);
    return std::string(reinterpret_cast<char*>(hash), SHA256_DIGEST_LENGTH);
}

// Integrity Verification Logic
bool verify_integrity(const TrinityLedger& ledger) {
    if (ledger.weather_data_size() == 0) return true;
    const auto& entry = ledger.weather_data(0);
    std::string data = std::to_string(entry.temperature()) + 
                       std::to_string(entry.humidity()) + 
                       std::to_string(entry.pressure()) +
                       std::to_string(entry.timestamp()) +
                       entry.sensor_id();
    return entry.entry_hash() == sha256(data);
}

int main() {
    TrinityLedger ledger;
    std::string path = "data/ledger.bin";

    // Load existing
    std::fstream input(path, std::ios::in | std::ios::binary);
    if (input && ledger.ParseFromIstream(&input)) {
        if (!verify_integrity(ledger)) {
            std::cerr << "!!! GOVERNANCE VIOLATION: DATA TAMPERED !!!" << std::endl;
            return 1;
        }
        std::cout << "--- TRINITY: STATE VALIDATED ---" << std::endl;
    } else {
        // Seed new
        auto* entry = ledger.add_weather_data();
        entry->set_temperature(72.0);
        entry->set_humidity(45.0);
        entry->set_pressure(1013.0);
        entry->set_timestamp(1717360000);
        entry->set_sensor_id("TRINITY_001");
        
        std::string data = std::to_string(entry->temperature()) + 
                           std::to_string(entry->humidity()) + 
                           std::to_string(entry->pressure()) +
                           std::to_string(entry->timestamp()) +
                           entry->sensor_id();
        entry->set_entry_hash(sha256(data));
        
        std::fstream output(path, std::ios::out | std::ios::trunc | std::ios::binary);
        ledger.SerializeToOstream(&output);
        std::cout << "--- TRINITY: ENVIRONMENTAL STATE COMMITTED ---" << std::endl;
    }
    return 0;
}
#include <openssl/evp.h> // Change from sha.h to evp.h

std::string sha256(const std::string str) {
    unsigned char hash[EVP_MAX_MD_SIZE];
    unsigned int length = 0;
    EVP_MD_CTX* context = EVP_MD_CTX_new();
    
    EVP_DigestInit_ex(context, EVP_sha256(), NULL);
    EVP_DigestUpdate(context, str.c_str(), str.size());
    EVP_DigestFinal_ex(context, hash, &length);
    EVP_MD_CTX_free(context);
    
    return std::string(reinterpret_cast<char*>(hash), length);
}

