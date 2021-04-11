def new_score():
	# creating global variables
	global sorted_scores_and_names, scores_and_names_dict, high_scores, another_score, names

	# asking whether the user want to add another score or save and print the current high scores
	another_score = input('do you want to add another score or save and print current high scores? (add/save) ')

	# adding a score if there are less than 5 currently entered
	while another_score == 'add' and len(high_scores) < 5:
		names.append(input('input new name'))
		high_scores.append(int(input('Input new high score')))
		scores_and_names_dict = dict(zip(names, high_scores))
		sorted_scores_and_names = sorted(scores_and_names_dict.items(), key=lambda x: x[1], reverse=True)
		print(sorted_scores_and_names)
		another_score = input('do you want to add another score or save and print current high scores? (add/save) ')

	# determine whether the new score is higher than the previous 5 scores and sorting accordingly
	while another_score == 'add' and len(high_scores) > 4:
		name = input('input new name')
		score = int(input('Input new high score'))
		if score > min(high_scores) and another_score == 'add':
			min_score_index = high_scores.index(min(high_scores))
			names.pop(min_score_index)
			names.append(name)
			high_scores.pop(min_score_index)
			high_scores.append(score)
			scores_and_names_dict = dict(zip(names, high_scores))
			sorted_scores_and_names = sorted(scores_and_names_dict.items(), key=lambda x: x[1], reverse=True)
			print(sorted_scores_and_names)
			another_score = input('do you want to add another score or save (add/save) ')
		else:
			print(
				'Sorry, your high score is lower than the current number 5 high score. To add a new score please re-run the script')

	# open or create file scores.txt and save the sorted high scores to scores.txt
	if len(high_scores) < 6 and another_score == 'save':
		with open("scores.txt", "w+") as f:
			f.write('high scores: ')
			scores_and_names_dict = dict(zip(names, high_scores))
			sorted_scores_and_names = sorted(scores_and_names_dict.items(), key=lambda x: x[1], reverse=True)
			print(sorted_scores_and_names)
			f.write(str(sorted_scores_and_names))
			f.write('\n')


sorted_scores_and_names = {}
scores_and_names_dict = {}
high_scores = []
names = []
new_score()
