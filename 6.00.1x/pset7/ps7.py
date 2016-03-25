import random
import math
import string

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        self.location = tuple(float(x) for x in location)
        self.species_types = species_types

    def get_number_of_species(self, animal):
        return self.species_types.get(animal, 0)

    def get_location(self):
        return self.location

    def get_species_count(self):
        return self.species_types.copy()

    def get_name(self):
        return self.name

    def adopt_pet(self, species):
        if species in self.species_types.keys():
            self.species_types[species] -= 1

            if self.species_types[species] == 0:
                self.species_types.pop(species)


class Adopter:
    """
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species

    def get_name(self):
        return self.name

    def get_desired_species(self):
        return self.desired_species

    def get_score(self, adoption_center):
        return 1.0 * adoption_center.get_number_of_species(self.desired_species)


class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species

    def get_score(self, adoption_center):
        desired_score = Adopter.get_score(self, adoption_center)
        considered_score = 0.3 * sum([adoption_center.get_number_of_species(x) for x in self.considered_species])
        total_score = desired_score + considered_score
        return total_score


class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species

    def get_score(self, adoption_center):
        desired_score = Adopter.get_score(self, adoption_center)
        feared_score = 0.3 * adoption_center.get_number_of_species(self.feared_species)
        total_score = desired_score - feared_score

        if total_score > 0:
            return total_score
        else:
            return 0.0

class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species

    def get_score(self, adoption_center):
        desired_score = Adopter.get_score(self, adoption_center)

        for species in self.allergic_species:
            if species in adoption_center.get_species_count().keys():
                return 0.0

        return desired_score


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter.
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary.
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness

    def get_score(self, adoption_center):
        desired_score = Adopter.get_score(self, adoption_center)

        # Use python built-in set intersection
        allergic_intersection = set(adoption_center.get_species_count().keys()) & set(self.allergic_species)

        # List of medical effectivness against allergic species Adoption Center contains
        intersection_medicine = [self.medicine_effectiveness[species] for species in allergic_intersection]

        # If there's no allergic species in Adoption Center just return a desired score
        try:
            return desired_score * min(contains_medicine)
        except:
            return desired_score

class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7) times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = location

    def get_linear_distance(self, to_location):
        # Basic pythagorean formula to find a distance between 2 points on a plane
        x1, y1 = self.location
        x2, y2 = to_location
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def get_score(self, adoption_center):
        distance = self.get_linear_distance(adoption_center.get_location())
        desired_species = adoption_center.get_number_of_species(self.desired_species)

        if distance < 1:
            return 1 * desired_species
        elif distance < 3:
            return random.uniform(0.7, 0.9) * desired_species
        elif distance < 5:
            return random.uniform(0.5, 0.7) * desired_species
        else:
            return random.uniform(0.1, 0.5) * desired_species


def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center
    such that the scores for each AdoptionCenter to the Adopter
    will be ordered from highest score to lowest score.
    """
    ranking = []

    for ac in list_of_adoption_centers:
        ranking.append([ac, adopter.get_score(ac)])

    # Sort by score first, in case of duplicates - sort by center's name
    ranking = sorted(ranking, key=lambda x: x[0].get_name())
    ranking = sorted(ranking, key=lambda x: x[1], reverse=True)
    return [ac[0] for ac in ranking]

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters
    from list_of_adopters (in numerical order of score)
    """
    ranking = []

    for ad in list_of_adopters:
        ranking.append([ad, ad.get_score(adoption_center)])

    # Sort by score first, in case of duplicates - sort by adopters's name
    ranking = sorted(ranking, key=lambda x: x[0].get_name())
    ranking = sorted(ranking, key=lambda x: x[1], reverse=True)
    return [x[0] for x in ranking[0:n]]
