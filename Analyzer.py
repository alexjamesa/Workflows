#!/usr/bin/env python

class Analyzer:

	@staticmethod
	def workflows_for_keywords( keyword_set,workflows ):
		matches = []
		scores = []
		for workflow in workflows:
			score = Analyzer._score( workflow,keyword_set )
			if score > 0:
				matches.append(workflow)
				scores.append(score)
		sorted_workflows = [x for (y,x) in sorted(zip(scores,matches),reverse=True)]
		return sorted_workflows

	@staticmethod
	def _score( workflow,keyword_set ): # Could be cleaned up!
		name_score = Analyzer._score_for_keywords( keyword_set.name, workflow.name )
		body_score = Analyzer._score_for_keywords( keyword_set.body, workflow.body )
		tags_score = Analyzer._score_for_keywords( keyword_set.tags, workflow.tags )

		all_content = " ".join([workflow.name,workflow.body,workflow.tags])
		wild_score = Analyzer._score_for_keywords( keyword_set.wild, all_content )

		smart_content = " ".join([workflow.name,workflow.name,workflow.name,workflow.body,workflow.tags,workflow.tags])
		smart_score = Analyzer._score_for_keywords( keyword_set.smart, smart_content ) / 2.0

		if name_score == 0 and len(keyword_set.name) > 0:
			return 0
		elif body_score == 0 and len(keyword_set.body) > 0:
			return 0
		elif tags_score == 0 and len(keyword_set.tags) > 0:
			return 0
		elif wild_score == 0 and len(keyword_set.wild) > 0:
			return 0
		elif smart_score == 0 and len(keyword_set.smart) > 0:
			return 0

		return name_score + body_score + tags_score + wild_score + smart_score

	@staticmethod
	def _score_for_keywords( keywords, content):
		score = 0
		for keyword in keywords:
			this_score = content.lower().count(keyword.lower()) 
			if this_score == 0:
				return 0
			score += this_score
		return score