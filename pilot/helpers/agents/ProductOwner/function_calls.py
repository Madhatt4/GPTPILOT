PROJECT_INCEPTION = {
    'definitions': [
        {
            'name': 'clarifying_question',
            'description': 'Use this if you have any clarifying questions or need to respond to a question from the user.'
                           'You must only ask one question at a time. If you have any more questions you must wait until '
                           'after the user responds to this question/response.',
            'parameters': {
                'type': 'object',
                'description': '...',
                'properties': {
                    # 'thoughts': {
                    #     'type': 'string',
                    #     'description': 'Any thoughts you have about the project so far and why you need to ask this question',
                    # },
                    # 'reasoning': {
                    #     'type': 'string',
                    #     'description': 'Your reasoning for asking this question',
                    # },
                    'type': {
                        'type': 'string',
                        'description': 'Set to `question` if you, the large language model, are asking a question to the user. '
                                       'Only set to `response` if the user has just asked a question to which you are responding. '
                                       'If everything is clear and you have no more questions, set this to `EVERYTHING_CLEAR`.',
                        'enum': ['question', 'response', 'EVERYTHING_CLEAR'],
                    },
                    'text': {
                        'type': 'string',
                        'description': 'A new question or a response to a question from the user. Required if `type` is `question` or `response`.'
                    },
                },
                'required': ['type']
            }
        }, {
            'name': 'project_description',
            'description': 'Provides a high level project summary, long term vision and lists immediate goals, non-functional requirements and out-of scope items',
            'parameters': {
                'type': 'object',
                'description': '...',
                'properties': {
                    'high_level_project_summary': {
                        'type': 'string',
                        'description': 'Product design - user experience, visual design',
                    },
                    'long_term_vision': {
                        'type': 'string',
                        'description': 'What is the long-term vision for the project?',
                    },
                    'immediate_goals': {
                        'type': 'array',
                        'description': 'High priority actionable goals to be achieved for the MVP. '
                                       'All goals should be specific, measurable and achievable',
                        'items': {
                            'type': 'string',
                        }
                    },
                    'non_functional_requirements': {
                        'type': 'array',
                        'description': 'Non-functional requirements - performance, security, reliability, scalability, '
                                       'availability, serviceability, usability, maintainability, extensibility, '
                                       'portability, compatibility, configurability, interoperability, '
                                       'internationalization, localization, regulatory, legal, privacy, '
                                       'accessibility, etc.',
                        'items': {
                            'type': 'string',
                        }
                    },
                    'out_of_scope': {
                        'type': 'array',
                        'description': 'Goals, features, or functionality that are out of scope for the MVP',
                        'items': {
                            'type': 'string',
                        }
                    }
                    # 'goals': {
                    #     # business goals - engineering efficiency, handling of customer growth, paid version,
                    #     # product goals - product readiness
                    #     # SLA - reliability, serviceability, scalability, availability, performance, security,
                    #     # out of scope
                    # }
                    # 'risks
                    # actors/roles (internal & external
                }
            }
        }
    ]
}
