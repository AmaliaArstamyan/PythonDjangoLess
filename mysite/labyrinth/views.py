from django.shortcuts import render

def maze_view(request):
    # Example maze data: 2D list of integers
    maze = [
        [1, 3],
        [0, 2]
    ]

    # Process the maze to add cell classes
    processed_maze = [
        [
            {
                "right": cell & 1,
                "bottom": cell & 2,
            }
            for cell in row
        ]
        for row in maze
    ]

    return render(request, 'labyrinth/labyrinth.html', {'maze': processed_maze})

