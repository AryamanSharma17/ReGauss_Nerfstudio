from plyfile import PlyData, PlyElement
import numpy as np
import time

def prune_points(input_file, output_file, sphere_center, sphere_radius):
    # Read PLY file
    plydata = PlyData.read(input_file)

    # Extract vertices
    vertices = plydata['vertex']
    print(vertices)

    # Create a list to hold pruned vertices
    pruned_vertices = []

    # Iterate through vertices
    for vertex in vertices:
        # Check if the vertex is within the sphere
        if is_within_sphere(vertex, sphere_center, sphere_radius):
            pruned_vertices.append(vertex)
    pruned_vertices = np.array(pruned_vertices)


    pruned_element = PlyElement.describe(pruned_vertices, 'vertex')

    # Write pruned vertices to a new PLY file
    pruned_element.text = False
    PlyData([pruned_element]).write(output_file)

def is_within_sphere(vertex, sphere_center, sphere_radius):
    # Calculate distance between vertex and sphere center
    distance = ((vertex['x'] - sphere_center[0])**2 +
                (vertex['y'] - sphere_center[1])**2 +
                (vertex['z'] - sphere_center[2])**2) ** 0.5
    
    # Check if the distance is less than or equal to the sphere radius
    return distance <= sphere_radius

# Example usage
input_file = '/home/sa11799x/Documents/Thesis_Aryaman/nerfstudio/DATA/0304_multidome_textured/Dragon/rad5/exports/splat/splat.ply'
output_file = '/home/sa11799x/Documents/Thesis_Aryaman/nerfstudio/DATA/0304_multidome_textured/Dragon/rad5/exports/splat/splat_pruned.ply'
sphere_center = (0, 0, 0)  # Example sphere center
sphere_radius = 0.5  # Example sphere radius
start = time.time()
prune_points(input_file, output_file, sphere_center, sphere_radius)
end = time.time()
print(f"Time taken: {end - start} seconds")
