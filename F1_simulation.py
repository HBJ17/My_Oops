from abc import ABC, abstractmethod
import random

# ---------------- ABSTRACT CLASS ----------------
class RaceRules(ABC):
    @abstractmethod
    def apply_safety_car(self):
        pass


# ---------------- BASE CLASS ----------------
class Vehicle:
    def __init__(self, engine_power):
        self.engine_power = engine_power


# ---------------- INHERITED CLASS ----------------
class F1Car(Vehicle):
    def __init__(self, engine_power, tyre):
        super().__init__(engine_power)
        self.tyre = tyre
        self.speed = self.calculate_speed()

    def calculate_speed(self):
        if self.tyre == "Soft":
            return self.engine_power + 30
        elif self.tyre == "Medium":
            return self.engine_power + 20
        else:
            return self.engine_power + 10

    def change_tyre(self, tyre):
        self.tyre = tyre
        self.speed = self.calculate_speed()


# ---------------- DRIVER CLASS (ENCAPSULATION) ----------------
class Driver:
    def __init__(self, name, team, car):
        self.name = name
        self.team = team
        self.car = car
        self.__position = 0   # private variable

    def set_position(self, pos):
        self.__position = pos

    def get_position(self):
        return self.__position

    def overtake(self):
        print(f"{self.name} is attempting an overtake!")


# ---------------- POLYMORPHISM ----------------
class AggressiveDriver(Driver):
    def overtake(self):
        print(f"{self.name} makes an aggressive overtake 🚀")


class DefensiveDriver(Driver):
    def overtake(self):
        print(f"{self.name} defends position carefully 🛡️")


# ---------------- RACE CLASS ----------------
class Race(RaceRules):
    def __init__(self, drivers, laps):
        self.drivers = drivers
        self.laps = laps
        self.safety_car = False

    def apply_safety_car(self):
        self.safety_car = True
        print("\n🚨 SAFETY CAR DEPLOYED!")
        for d in self.drivers:
            d.car.speed -= 20

    def start_race(self):
        print("\n🏁 Race Started at Abu Dhabi Grand Prix 2021\n")

        for lap in range(1, self.laps + 1):
            print(f"--- Lap {lap} ---")

            if lap == self.laps - 1:
                self.apply_safety_car()

            if lap == self.laps:
                print("\n🏎️ FINAL LAP ACTION!\n")
                for d in self.drivers:
                    d.overtake()

        self.finish_race()

    def finish_race(self):
        # Sort drivers by speed (simple simulation logic)
        self.drivers.sort(key=lambda d: d.car.speed, reverse=True)

        print("\n🏆 FINAL RESULTS 🏆")
        for i, d in enumerate(self.drivers, start=1):
            d.set_position(i)
            print(f"{i}. {d.name} ({d.team})")

        print(f"\n🥇 Winner: {self.drivers[0].name}")


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":

    # Cars
    redbull_car = F1Car(engine_power=300, tyre="Soft")
    mercedes_car = F1Car(engine_power=295, tyre="Hard")

    # Drivers
    verstappen = AggressiveDriver("Max Verstappen", "Red Bull Racing", redbull_car)
    hamilton = DefensiveDriver("Lewis Hamilton", "Mercedes", mercedes_car)

    drivers = [verstappen, hamilton]

    # Race
    abu_dhabi_race = Race(drivers, laps=5)
    abu_dhabi_race.start_race()
