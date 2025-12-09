import xml.etree.ElementTree as ET
from typing import List, Dict, Any

def load_users_data(file_path: str = "users.xml"):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        users = []
        for user_elem in root.findall('user'):
            user = {
                'user_id': int(user_elem.find('user_id').text),
                'name': user_elem.find('name').text,
                'age': int(user_elem.find('age').text),
                'weight': int(user_elem.find('weight').text),
                'fitness_level': user_elem.find('fitness_level').text
            }
            users.append(user)
        return users
    except FileNotFoundError:
        print("File not found")
        return []
    except Exception as e:
        print("Exception error")
        return []

def load_workouts_data(file_path: str = "workouts.xml"):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        workouts = []
        for workouts_elem in root.findall('workout'):
            workout = {
                'workout_id': int(workouts_elem.find('workout_id').text),
                'user_id': int(workouts_elem.find('user_id').text),
                'date': workouts_elem.find('date').text,
                'type': workouts_elem.find('type'),
                'duration': int(workouts_elem.find('duration').text),
                'distance': float(workouts_elem.find('distance').text),
                'calories': int(workouts_elem.find('calories').text),
                'avg_heart_rate': int(workouts_elem.find('avg_heart_rate').text),
                'intensity': workouts_elem.find('intensity').text
            }
            workouts.append(workout)
        return workout
    except FileNotFoundError:
        print("File not found")
        return []
    except Exception:
        print("Exception error")
        return []

def get_stats(users: List[Dict[str, Any]], workouts: List[Dict[str, Any]]):
    if not workouts:
        return {
            'total_workouts': 0,
            'total_users': 0,
            'total_calories': 0,
            'total_duration_hours': 0.0,
            'total_distance_km': 0.0
        }
    total_workouts = len(workouts)

    user_ids = set(w['user_id'] for w in workouts)
    total_users = len(user_ids)

    total_calories = sum(w['calories'] for w in workouts)

    total_duration_min = sum(w['duration'] for w in workouts)
    total_duration_hours = total_duration_min / 60.0

    total_distance_km = sum(w['distance'] for w in workouts)

    return {
        'total_workouts': total_workouts,
        'total_users': total_users,
        'total_calories': total_calories,
        'total_duration_hours': total_duration_hours,
        'total_distance_km': total_distance_km
    }

def print_stats(stats: Dict[str, Any]):
    print("STATS")
    print("=" * 50)
    print(f"Total workouts: {stats['total_workouts']}")
    print(f"Total users: {stats['total_users']}")
    print(f"Total calories: {stats['total_calories']}")
    print(f"Total time: {stats['total_duration_hours']:.1f} h")
    print(f"Total distance: {stats['total_distance_km']:.1f} km")

users = load_users_data("users.xml")
workouts = load_workouts_data("workouts.xml")

stats = get_stats(users, workouts)
print_stats(stats)