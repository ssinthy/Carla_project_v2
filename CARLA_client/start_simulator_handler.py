def start_simulation_pressed_handler(self):
        road_type = self.comboBox_road_type.currentText()
        ego_position = self.comboBox_ego_position.currentText()
        emv_position = self.comboBox_emv_position.currentText()
        emv_travel_direction = self.comboBox_emv_travel_direction.currentText()
        weather_condition = self.comboBox_weather.currentText()
        time_of_day = self.comboBox_time_of_day.currentText()
        print(road_type, ego_position, emv_position, emv_travel_direction)
        
        scenario_info = {
                "road_type": road_type,
                "ego_position": ego_position,
                "emv_position": emv_position,
                "emv_travel_direction": emv_travel_direction
            }
        
        print(scenario_info)