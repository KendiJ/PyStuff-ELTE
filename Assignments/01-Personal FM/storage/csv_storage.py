import csv
import os
from exceptions import StorageError

class CSVStorage:
    @staticmethod
    def save(filename, data, fieldname):
        """
        Writes data to a temporary file first, then renames it to the actual filename.
        This ensures that if the program crashes during write, the original file is not corrupted.
        """
        temp_filename = filename + ".tmp"
        try:
            with open(temp_filename, mode="w", newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldname=fieldname)
                writer.writeheader()
                writer.writerows(data)

            if os.path.exists(filename):
                os.remove(filename)
            os.rename(temp_filename, filename)
    
        except IOError as e:
            if os.path.exists(temp_filename):
                os.remove(temp_filename)
            raise StorageError(f"Failed to save to {fieldname}: {e}")
        
    @staticmethod
    def load(filename):
        if not os.path.exists(filename):
            return []
        
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return list(reader)
        except IOError as e:
            raise StorageError(f"failed to load from file {filename}: {e}")
        
