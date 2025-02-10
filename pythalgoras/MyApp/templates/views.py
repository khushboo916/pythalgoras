def fifthview(request):
    context = {'name':’khushboo’'}
    return render(request, 'MyApp/introduction_to_ai.html',context)
