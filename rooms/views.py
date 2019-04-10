
def room_render(request, roomID):
  context = {'slug':roomID}
  return render(request, 'room.html', context)