import os
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodDance_web.settings')

import django

django.setup()
from fooddance.models import *;
from django.conf import settings
from django.core.files.images import ImageFile


def populate():
    users = [
        {'username': 'test1', 'password': 'test123', 'email': 'test1@test.com', 'image': 'avatars/avatar_test.jpg'},
        {'username': 'test2', 'password': 'test123', 'email': 'test2@test.com', 'image': 'avatars/avatar_test2.jpg'},
        {'username': 'test3', 'password': 'test123', 'email': 'test3@test.com', 'image': 'avatars/avatar_test3.jpg'},
        {'username': 'test4', 'passowrd': 'test123', 'email': 'test4@test.com', 'image': 'avatars/avatar_test4.jpg'},
        {'username': 'test5', 'password': 'test123', 'email': 'test5@test.com', 'image': 'avatars/avatar_test5.jpg'},
    ]

    recipes = [
        {'title': 'Vegan Cheesecake',
         'author': 'test1',
         'image': 'recipes/vegan-cheesecake.jpeg',# required!!!!
         'overview':
            "This no-bake vegan cheesecake, with its boozy Black Forest cherry topping, is a luxurious twist on a "
            "retro classic. It's completely delicious and just the thing for celebrations and parties. See the recipe "
            "tips for alternative topping ideas.For this recipe you will need a food processor or blender.",
         'duration': 30,
         'budget': 10,
         'difficulty': 5,
         'materials': [
             {'ingredient': 'vegan bourbon biscuits', 'weight': '200g'},
             {'ingredient': 'dairy-free margarine', 'weight': '75g'},
             {'ingredient': 'vegan dark chocolate', 'weight': '350g'},
             {'ingredient': 'cocoa butter', 'weight': '50g'},
             {'ingredient': 'extra-firm silken tofu', 'weight': '400g'},
         ],
         'steps': [
             {'image': 'recipes/vegan-cheesecake_1.jpg',
                 'content': 'Grease a deep 20cm/8in round springform cake tin and line the base and sides with baking paper.'},
             {'content': 'Mix the crushed biscuits with the melted margarine and 2 pinches of salt, spread evenly over the base of the prepared tin and press down firmly. Place in the fridge for 40 minutes.'},
             {'content': 'Melt the chocolate and cocoa butter (or coconut oil) in a heatproof bowl over a pan of gently simmering water, stirring occasionally, until smooth.'},
             {'content': 'Put the tofu, vanilla, sugar and oat crème fraiche into a blender or food processor and blend until smooth. Add the melted chocolate mixture and blend again, then add a pinch of salt. Spread over the chilled base and smooth the top. Place in the fridge for at least 4 hours or, better still, overnight.'},
             {'content': 'You can make the cherry compôte in advance, but keep it separate until serving. Put the cherries into a saucepan, add the cornflour and stir until all are coated. Pour in 2 tablespoons of the kirsch, the sugar and 100ml/3½fl oz water. Stir over a medium heat for 5–6 minutes, simmering gently until the sauce has thickened and the cherries are soft. Remove from the heat and stir in the remaining tablespoon of kirsch, adding lemon juice to taste. Cool, then place in the fridge if making ahead.'},
             {'content': 'To serve, carefully remove the cheesecake from the tin, peel away the lining paper and put the cheesecake on a serving plate. Spoon the boozy cherry compôte (warm, or stirred to loosen if chilled) over the cheesecake, letting the syrup and fruit run down the sides'},
         ],
         'comments': [
             {'user': 'test2', 'rating': 3, 'content': "I’d really like some ca-me:"},
             {'user': 'test3', 'rating': 2, 'content': "This cake is absolutely perfect it's so soft and delicious wow just wow"},
             {'user': 'test2', 'rating': 5, 'content': "i could really go for some cake me asf:"},
         ]
         },
         
        {    'title': 'Paella mixta',
             'author': 'test2',
             'image': 'recipes/paella-mixta.jpg',
             'overview':
                "Try our version of paella, made with a combination of meat and seafood. With king prawns, mussels, chorizo 
                "and chicken, every forkful is a treat that's reminiscent of Spanish holidays",
            'duration': 75,
            'budget': 20,
            'diffcutly': 5,
            'materials':[
                 {'ingredient': 'chopped tomatoes', 'weight': '400g'},
                 {'ingredient': 'chicken stock', 'weight': '600g'},
                 {'ingredient': 'smoked paprika', 'weight': '50g'},
                 {'ingredient': 'saffron', 'weight': '20g'},
                 {'ingredient': 'garlic cloves', 'weight': '40g'},
                 {'ingredient': 'olive oil', 'weight': '20g'},
                 {'ingredient': 'paella rice', 'weight': '300g'},
                 {'ingredient': 'chicken thighs', 'weight': '100g'},
                 {'ingredient': 'chorizo', 'weight': '200g'},
                 {'ingredient': 'frozen pease', 'weight': '85g'},
                 {'ingredient': 'raw king prawns', 'weight': '150g'},
                 {'ingredient': 'mussels', 'weight': '250g'},
                 {'ingredient': 'lemon', 'weight': '40g'},
            ],
            'steps': [
                {'content' : 'Heat the oven to 220C/200C fan/gas 7. Combine the tomatoes, stock, paprika and saffron in a large heatproof jug.'},
                {'content' : 'Then microwave the mixture for 5 mins on high, or until steaming hot. Or, heat in a pan on the hob.'},
                {'content' : 'Put the onion and garlic in a large ovenproof frying pan or roasting tin, drizzle over the olive oil and stir to coat.'},
                {'content' : 'Roast for 20 mins, or until the veg is starting to brown.'},
                {'content' : 'Stir in the rice, chicken, chorizo and hot stock mix. Season and bake for 20 mins (don’t cover the pan).'},
                {'content' : 'Gently stir in the peas, dot over the prawns and press the mussels in, hinged-side down, so they’re standing up. Arrange the lemon wedges around the edge, if using.'},
                {'content' : 'Bake for 5-10 mins more until the rice, chicken and prawns are cooked, and the mussels have opened (discard any that stay shut). Check for seasoning, and serve.'},
            ],
            'comments': [
                {'user': 'test4', 'rating': 2, 'content':"It costs too much time"},
                {'user': 'test5', 'rating': 1, 'content':"It is tooooo diffcult! give a easy vesion plz"},
                {'user': 'test1', 'rating': 5, 'content':"Super yummy! totally worth my time"},
                {'user': 'test3', 'rating': 4, 'content':"will do this again!"},
            ]
         },
         
         {  'title': 'Ramen noodle',
            'author': 'test2',
            'image': 'recipes/ramen-noodle.jpg'
            'overview':
                "Use chicken, noodles, spinach, sweetcorn and eggs to make this moreish Japanese noodle soup, for when you crave something comforting yet light and wholesome."
            'duration': 20,
            'budget': 10,
            'difficulty': 5,
            'materials': [
                 {'ingredient': 'chicken stock', 'weight': '700g'},
                 {'ingredient': 'garlic cloves', 'weight': '150g'},
                 {'ingredient': 'soy souce', 'weight': '40g'},
                 {'ingredient': 'Worcestershire sauce', 'weight': '10g'},
                 {'ingredient': 'ginger', 'weight': '5g'},
                 {'ingredient': 'Chinese five spice', 'weight': '5g'},
                 {'ingredient': 'chili powder', 'weight': '3g'},
                 {'ingredient': 'ramen noodles', 'weight': '375g'},
                 {'ingredient': 'cooked pork', 'weight': '400g'},
                 {'ingredient': 'sesame oil', 'weight': '20g'},
            ],
            'steps': [
                {'content': 'Mix 700ml chicken stock, 3 halved garlic cloves, 4 tbsp soy sauce, 1 tsp Worcestershire sauce, a sliced thumb-sized piece of ginger, ½ tsp Chinese five spice, pinch of chilli powder and 300ml water in a stockpot or large saucepan, bring to the boil, then reduce the heat and simmer for 5 mins.'},
                {'content': 'Taste the stock – add 1 tsp white sugar or a little more soy sauce to make it sweeter or saltier to your liking.'},
                {'content': 'Cook 375g ramen noodles following the pack instructions, then drain and set aside.'},
                {'content': 'Slice 400g cooked pork or chicken, fry in 2 tsp sesame oil until just starting to brown, then set aside.'},
                {'content': 'Divide the noodles between four bowls.'},
            ],
            'comments': [
                {'user': 'test1', 'rating': 2, 'content':"It's easy...just not tasty"},
                {'user': 'test5', 'rating': 3, 'content':"40 pounds cheaper than a high street chain wag"},
            ]
         },
         
         {  'title': 'Chocolate cake',
            'author': 'test1',
            'image': 'recipes/chocolate-cake.jpg'
            'overview':
                "Need a guaranteed crowd-pleasing cake that's easy to make?"
                "This super-squidgy chocolate fudge cake with smooth icing is an instant baking win.",
            'duration': 45,
            'budget': 25,
            'difficulty': 5,
            'materials': [
                {'ingredient': 'sunflower oil', 'weight': '150g'},
                {'ingredient': 'self-raising flour', 'weight': '170g'},
                {'ingredient': 'cooca powder', 'weight': '10g'},
                {'ingredient': 'icarbonate of soda', 'weight': '5g'},
                {'ingredient': 'caster sugar', 'weight': '150g'},
                {'ingredient': 'golden syrup', 'weight': '5g'},
                {'ingredient': 'large eggs', 'weight': '120g'},
                {'ingredient': 'semi-skimmed milk', 'weight': '150g'},
                {'ingredient': 'unsalted butter', 'weight': '100g'},
                {'ingredient': 'icing sugar', 'weight': '225g'},
            ],
            'steps': [
                {'content': 'Heat the oven to 180C/160C fan/gas 4. Oil and line the base of two 18cm sandwich tins. '},
                {'content': 'Sieve the flour, cocoa powder and bicarbonate of soda into a bowl. Add the caster sugar and mix well.'},
                {'content': 'Make a well in the centre and add the golden syrup, eggs, sunflower oil and milk. Beat well with an electric whisk until smooth.'},
                {'content': 'Pour the mixture into the two tins and bake for 25-30 mins until risen and firm to the touch.'},
                {'content': 'Remove from oven, leave to cool for 10 mins before turning out onto a cooling rack.'},
                {'content': 'To make the icing, beat the unsalted butter in a bowl until soft. Gradually sieve and beat in the icing sugar and cocoa powder, then add enough of the milk to make the icing fluffy and spreadable.'},                
            ],
            'comments': [
                {'user': 'test2', 'rating': 5, 'content':"Cannot wait to have one"},
                {'user': 'test3', 'rating': 2, 'content':"My daughter really loves it! Fab recipe"},
                {'user': 'test5', 'rating': 1, 'content':"Hard to follow..."},
            ]
         },
         
         {  'title': 'Roast chicken',
            'author': 'test3',
            'image': 'recipes/roast-chicken.jpg'
            'overview':
                "What more can we say? A classic roast chicken recipe should be in everyone's repertoire, and it can always save the day.",
            'duration': 90,
            'budget': 30,
            'difficulty': 4,
            'materials': [
                {'ingredient': 'onion', 'weight': '50g'},
                {'ingredient': 'carrots', 'weight': '120g'},
                {'ingredient': 'chicken', 'weight': '1500g'},
                {'ingredient': 'lemon', 'weight': '30g'},
                {'ingredient': 'butter', 'weight': '25g'},
                {'ingredient': 'chicken stock', 'weight': '250g'},
            ],
            'steps': [
                {'content': 'Heat oven to 190C/fan 170C/gas 5. Have a shelf ready in the middle of the oven without any shelves above it.'},
                {'content': 'Scatter 1 roughly chopped onion and 2 roughly chopped carrots over the base of a roasting tin that fits the whole chicken, but doesn’t swamp it.'},
                {'content': 'Season the cavity of the chicken liberally with salt and pepper, then stuff with 2 lemon halves and a small bunch of thyme, if using.'},
                {'content': 'Sit the chicken on the vegetables, smother the breast and legs all over with 25g softened butter, then season the outside with salt and pepper.'},
                {'content': 'Place in the oven and leave, undisturbed, for 1 hr 20 mins – this will give you a perfectly roasted chicken.'},
                {'content': 'Carefully remove the tin from the oven and, using a pair of tongs, lift the chicken to a dish or board to rest for 15-20 mins. As you lift the dish, let any juices from the chicken pour out of the cavity into the roasting tin.'},
                {'content': 'While the chicken is resting, make the gravy. Place the roasting tin over a low flame, then stir in 1 tbsp flour and sizzle until you have a light brown, sandy paste.'},
                {'content': 'Gradually pour in 250ml chicken stock, stirring all the time, until you have a thickened sauce.'},
                {'content': 'Simmer for 2 mins, using a wooden spoon to stir, scraping any sticky bits from the tin.'},
                {'content': 'Strain the gravy into a small saucepan, then simmer and season to taste. When you carve the bird, add any extra juices to the gravy.'},
            ],
            'comments': [
                {'user': 'test2', 'rating': 4, 'content':"Super easy to follow! Thanks for sharing!"},
                {'user': 'test5', 'rating': 3, 'content':"Winter smell, got hugry already ;-)"},
                {'user': 'test1', 'rating': 2, 'content':"Got roasted..."},
                {'user': 'test2', 'rating': 4, 'content':"I made this for my dinner. will do it again!"},
            ]
         },
         
         {  'title': 'Tortilla pizza',
            'author': 'test2',
            'image': 'recipes/tortilla-pizza.jpg'
            'overview':
                "Make homemade sourdough pizza with a wonderfully chewy crust."
                "Try our margherita recipe, then customise with your favourite toppings.",
            'duration': 25,
            'budget': 13,
            'difficulty': 4,
            'materials': [
                {'ingredient': 'passata', 'weight': '400g'},
                {'ingredient': 'garlic', 'weight': '50g'},
                {'ingredient': 'olive oil', 'weight': '20g'},
                {'ingredient': 'dried herbs', 'weight': '30g'},
                {'ingredient': 'plain tortillas', 'weight': '20g'},
                {'ingredient': 'grated mozzarella', 'weight': '50g'},
                {'ingredient': 'pepperoni', 'weight': '80g'},
                {'ingredient': ' jalapeño', 'weight': '100g'},

            ],
            'steps': [
                 {'content': 'Heat the oven to 220C/200C fan/gas 7. Mix the passata, garlic, olive oil, herbs and season well.'},
                 {'content': 'Put the tortillas onto one large baking sheet, or two smaller ones.'},
                 {'content': 'Spread over the tomato sauce leaving a 1cm border around the edges.'},  
                 {'content': 'Scatter with the mozzarella, add the pepperoni and jalapenos. '},
                 {'content': 'Bake for 6-8 minutes until the edges of the tortillas are crisp and golden, and the cheese has melted and is bubbling.'},
            ],
            'comments': [
                 {'user': 'test3', 'rating': 3, 'content': "love this recipe! helps me alot"},
                 {'user': 'test4', 'rating': 2, 'content': "Why do I got a half-raw pasta? I followed all the steps"},
                 {'user': 'test4', 'rating': 1, 'content': "Waste my time, juice of tomatoes makes it super wet..."},
                 {'user': 'test1', 'rating': 4, 'content': "Good recipe, add tomatoes making it even delicious"},
            ]
         },
         
         {  'title': 'Sponge pudding',
            'author': 'test1',
            'image': 'recipes/sponge-pudding.jpg'
            'overview':
                "Transform a classic lemon drizzle cake into a self-saucing pud for a cheap, comforting dessert. Serve with cream or custard.",
            'duration': 65,
            'budget': 15,
            'difficulty': 4,
            'materials': [
                {'ingredient': 'soft butter', 'weight': '250g'},
                {'ingredient': 'caster sugar', 'weight': '380g'},
                {'ingredient': 'eggs', 'weight': '200g'},
                {'ingredient': 'self-raising flour', 'weight': '250g'},
                {'ingredient': 'baking powder', 'weight': '5g'},
                {'ingredient': 'lemons', 'weight': '180g'},
                {'ingredient': 'cornflour', 'weight': '180g'},
                {'ingredient': 'cream', 'weight': '200g'},
                {'ingredient': 'icing sugar', 'weight': '50g'},
            ],
            'steps': [
                {'content': 'Heat the oven to 180C/160C fan/gas 4. Butter a 30 x 20cm deep baking dish.'},
                {'content': 'Put the butter and 250g caster sugar in a bowl and beat for 5 mins until pale and fluffy.'},
                {'content': ' Whisk in the eggs, then sieve over the flour and baking powder and fold in until you have a batter. Stir in the lemon zest, reserving a little for decoration.'},
                {'content': 'Spoon the sponge batter into the dish and smooth over the top.'},
                {'content': 'Mix the lemon juice with the cornflour in a heatproof bowl to make a smooth paste. Mix the remaining 130g caster sugar with 300ml boiling water in a jug, pour over the cornflour mix and whisk until smooth. Pour this over the sponge. '},
                {'content': 'Bake for 45-50 mins until golden and set, and the sponge springs back when touched.'},
                {'content': 'While the pudding is baking, make the lemon drizzle. Mix the icing sugar with enough lemon juice (about half of it) to create a loose consistency. Drizzle over the sponge while it’s still warm and decorate with the reserved lemon zest. '},
                {'content': 'Serve straightaway with cream or custard.'},
            ],
            'comments': [
                {'user': 'test1', 'rating': 1, 'content':"Too much steps"},
                {'user': 'test4', 'rating': 2, 'content':"Very sour, is it just me..."},
                {'user': 'test9', 'rating': 4, 'content':"Yummy!"},
                {'user': 'test8', 'rating': 1, 'content':"Should not mix it directly"},                
            ]
         },
         
         {  'title': 'Beef curry',
            'author': 'test3',
            'image': 'recipes/beef-curry.jpg'
            'overview':
                "Make our easy beef curry and serve with a hunk of naan bread to mop up the delicious juices. If you prefer it less spicy, simply add less chilli powder."
            'duration': 170,
            'budget': 30,
            'difficulty': 4,
            'materials': [
                 {'ingredient': 'oil', 'weight': '20g'},
                 {'ingredient': 'braising steak', 'weight': '500g'},
                 {'ingredient': 'butter', 'weight': '25g'},
                 {'ingredient': 'onion', 'weight': '70g'},
                 {'ingredient': 'garlic cloves', 'weight': '90g'},
                 {'ingredient': 'giner', 'weight': '10g'},
                 {'ingredient': 'hot chili powder', 'weight': '3g'},
                 {'ingredient': 'turmeric', 'weight': '20g'},
                 {'ingredient': 'ground coriander', 'weight': '40g'},
                 {'ingredient': 'cardamom pods', 'weight': '100g'},
                 {'ingredient': 'tomatoes', 'weight': '400g'},
                 {'ingredient': 'beef stock', 'weight': '300g'},
                 {'ingredient': 'sugar', 'weight': '10g'},
                 {'ingredient': 'garam masala', 'weight': '20g'},
                 {'ingredient': 'double cream', 'weight': '20g'},
                 {'ingredient': 'bunch coriander', 'weight': '5g'},
            ],
            'steps': [
                {'content': 'Heat one tbsp of the oil in a casserole pot over a medium-high heat. Season the beef and fry in the pot for 5-8 mins, turning with a pair of tongs half way until evenly browned. Set aside on a plate.'},
                {'content': 'Heat the remaining oil and butter in the pan and add the onions. Fry gently for 15 mins or until golden brown and caramelised.'},
                {'content': 'Add the garlic, ginger, chilli, turmeric, ground coriander and cardamom and fry for two mins. Tip in the tomatoes, stock and sugar and bring to the simmer.'},
                {'content': 'Add the beef, put a lid on top of the curry and cook over a low heat for 1 ½ – 2 hrs or until the meat is tender and falling apart. Remove the lid for the last 20 minutes of cooking.'},
                {'content': 'Stir through the garam masala and cream (if using) and season to taste. Scatter over the coriander and serve with naan breads or rice.'},    
            ],
            'comments': [
                {'user': 'test2', 'rating':3 , 'content':"Looks great but what do you season the beef with please?"},
                {'user': 'test5', 'rating':4 , 'content':"I've made this three times in the last couple of months. It's delicious and everyone ate it."},
                {'user': 'test4', 'rating':1 , 'content':"Cooked with chicken, really horrible..."},
            ]
         },
         
         {  'title': 'Seafood pasta',
            'author': 'test2',
            'image': 'recipes/seafood-pasta.jpg'
            'overview':
                "Make a low in fat, satisfying dish in minutes – ideal for Friday nights"
            'duration': 15,
            'budget': 10,
            'difficulty': 3,
            'materials': [
                 {'ingredient': 'olive oil', 'weight': '25g'},
                 {'ingredient': 'onion', 'weight': '50g'},
                 {'ingredient': 'garlic clove', 'weight': '50g'},
                 {'ingredient': 'paprika', 'weight': '20g'},
                 {'ingredient': 'tomatoes', 'weight': '40g'},
                 {'ingredient': 'chicken stock', 'weight': '1000g'},
                 {'ingredient': 'spaghetti', 'weight': '300g'},
                 {'ingredient': 'frozen sedfood', 'weight': '240g'},
            ],
            'steps': [
                {'content': 'Heat the oil in a wok or large frying pan, then cook the onion and garlic over a medium heat for 5 mins until soft.'},
                {'content': 'Add the paprika, tomatoes and stock, then bring to the boil.'},
                {'content': 'Turn down the heat to a simmer, stir in the pasta and cook for 7 mins, stirring occasionally to stop the pasta from sticking.'},
                {'content': 'Stir in the seafood, cook for 3 mins more until it’s all heated through and the pasta is cooked, then season to taste.'},
            ],
            'comments': [
                {'user': 'test1', 'rating': 5, 'content':"Really liked this , made it for the family, kids loved it"},
                {'user': 'test3', 'rating': 3, 'content':"Cooked perfectly. Will definitely do this again!"},
                {'user': 'test4', 'rating': 4, 'content':"Quick,healthy and delicious! Fab recipe!"},
                {'user': 'test4', 'rating': 4, 'content':"Can you add cream, or creme fraiche to make it a creamy sauce?"},
                {'user': 'test5', 'rating': 1, 'content':"Worst thing I’ve ever spent my time and money on."},
            ]
         },
         
         {  'title': 'Beef stew',
            'author': 'test3',
            'image': 'recipes/beef-stew.jpg'
            'overview':
                "Cook beef stew in a slow cooker for really tender meat. Add button mushrooms or smoked paprika for extra flavour – it will be an instant family favourite.",
            'duration': 270,
            'budget': 40,
            'difficulty': 3,
            'materials': [
                 {'ingredient': 'onion', 'weight': '40g'},
                 {'ingredient': 'cerlery sticks', 'weight': '60g'},
                 {'ingredient': 'rapeseed oil', 'weight': '20g'},
                 {'ingredient': 'carrot', 'weight': '200g'},
                 {'ingredient': 'bay leaves', 'weight': '10g'},
                 {'ingredient': 'pack thyme', 'weight': '50g'},
                 {'ingredient': 'tomato puree', 'weight': '50g'},
                 {'ingredient': 'sauce', 'weight': '50g'},
                 {'ingredient': 'beef stock pots', 'weight': 'g'},
                 {'ingredient': 'beef', 'weight': '900g'},
                 {'ingredient': 'parsley', 'weight': '20g'},
                 {'ingredient': 'cornflour', 'weight': '20g'},
            ],
            'steps': [
                {'content': 'Fry the onion and celery in 1 tbsp oil over a low heat until they start to soften – about 5 mins.'},
                {'content': 'Add the carrots, bay and thyme, fry for 2 mins, stir in the purée and Worcestershire sauce, add 600ml boiling water, stir and tip everything into a slow cooker.'},
                {'content': 'Crumble over the stock cubes or add the stock pots and stir, then season with pepper (don’t add salt as the stock may be salty).'},
                {'content': 'Clean out the frying pan and fry the beef in the remaining oil in batches until it is well browned, then tip each batch into the slow cooker. Cook on low for 8-10 hrs, or on high for 4 hrs.'},
                {'content': 'If you want to thicken the gravy, mix the cornflour with a splash of cold water to make a paste, then stir in 2 tbsp of the liquid from the slow cooker.'},
                {'content': 'Tip back into the slow cooker, stir and cook for a further 30 mins on high. Stir in the parsley and season again to taste.'},
            ],
            'comments': [
                {'user': 'test4', 'rating': 5, 'content':"Absolutely delicious! So easy to make and everyone loves it."},
                {'user': 'test2', 'rating': 1, 'content':"Too time consuming to make it second time"},
                {'user': 'test5', 'rating': 5, 'content':"It's my first time cooking beef and I followed this recipe. Too delicious to believe it's my own work!"},
            ]
         },
         
         {  'title': 'Rice pudding',
            'author': 'test1',
            'image': 'recipes/rice-pudding.jpg'
            'overview':
                "Try our recipe for a gorgeously creamy, yet low in fat rice pudding. Serve this comforting dessert with jam or fruit.",
            'duration': 70,
            'budget': 3,
            'difficulty': 1,
            'materials': [
                {'ingredient': 'pudding rices', 'weight': '100g'},
                {'ingredient': 'butter', 'weight': '80g'},
                {'ingredient': 'sugar', 'weight': '50g'},
                {'ingredient': 'milk', 'weight': '700g'},
                {'ingredient': 'lemon zest', 'weight': '5g'},
                {'ingredient': 'leaf', 'weight': '5g'},
            ],
            'steps': [
                {'content': 'Heat the oven to 150C/130C fan/gas 2. Wash and drain the rice.'},
                {'content': 'Butter a 850ml baking dish, then tip in the rice and sugar and stir through the milk. Sprinkle in the nutmeg and top with the bay leaf or lemon zest.'},
                {'content': 'Cook for 2 hrs or until the pudding wobbles ever so slightly when shaken.'},
            ],
            'comments': [
                {'user': 'test5', 'rating': 4, 'content':"Easy and yummy!"},
                {'user': 'test3', 'rating': 3, 'content':"best dinner disert"},
            ]
         },
         
    ]

    collections = [
        {
            'user': 'test1', 'recipe': 'Paella mixta',
            'user': 'test1', 'recipe': 'Beef curry',
            'user': 'test1', 'recipe': 'Seafood pasta',
        },
        {
            'user': 'test2', 'recipe': 'Vegan Cheesecake',
            'user': 'test2', 'recipe': 'Seafood pasta',
        },
        {
            'user': 'test3', 'recipe': 'Roast chicken',
        },
        {
            'user': 'test4', 'recipe': 'Vegan Cheesecake',
            'user': 'test4', 'recipe': 'Beef Stew',
            'user': 'test4', 'recipe': 'Paella mixta',
            'user': 'test4', 'recipe': 'Ramen noodle',
        },
        {
            'user': 'test5', 'recipe': 'Sponge pudding',
            'user': 'test5', 'recipe': 'Chocolate cake',
            'user': 'test5', 'recipe': 'Rice pudding',
        },
    ]

    for user in users:
        image = None
        if 'image' in user.keys():
            image = user['image']

        user = add_user(user['username'], user['password'], user['email'], image)
        print(f'- {user}')

    for recipe in recipes:

        image = None
        if 'image' in recipe.keys():
            image = recipe['image']

        add_recipe(recipe['title'], recipe['author'], recipe['overview'], recipe['duration'],
                   recipe['budget'], recipe['difficulty'], recipe['materials'], recipe['steps'],
                   recipe['comments'], image)

    for collection in collections:
        u = add_collection(collection['user'], collection['recipe'])
        print(f"- {collection['user']} collect {collection['recipe']}")


def add_user(username, password, email, image=None):
    user = User.objects.get_or_create(username=username, password=password, email=email)[0]

    user.save()
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    if image:
        userprofile.image = os.path.join(image)
        print(f'- add image {image}')

    userprofile.save()
    return user


def add_recipe(title, author_name, overview, duration, budget, difficulty, materials, steps, comments, image=None):
    author = User.objects.get(username=author_name)

    r = Recipe.objects.get_or_create(title=title, author=author, overview=overview, duration=duration,
                                     budget=budget, difficulty=difficulty)[0]
    if image:
        r.image = os.path.join(image)
        print(f'- add image {image}')

    r.save()

    print(f'- {r}')
    for material in materials:
        m = add_material(r, material['ingredient'], material['weight'])
        print(f'- {m}')

    for step in steps:
        image = None
        if 'image' in step.keys():
            image = step['image']

        s = add_step(r, step['content'],image)
        print(f'- {s}')

    for comment in comments:
        c = add_comment(comment['user'], r, comment['rating'], comment['content'])
        print(f'- {c}')

    return r


def add_material(recipe, ingredient, weight):
    m = Materials.objects.get_or_create(recipe=recipe, ingredient=ingredient, weight=weight)[0]
    m.save()
    return m


def add_step(recipe, content, image=None):
    s = RecipeStep.objects.get_or_create(recipe=recipe, content=content)[0]
    if image:
        s.image = os.path.join(image)
        print(f'- add image {image}')
    s.save()
    time.sleep(0.5)
    return s


def add_comment(user_name, recipe, rating, content):
    u = User.objects.get(username=user_name)
    c = Comment.objects.get_or_create(recipe=recipe, user=u, rating=rating, content=content)[0]
    c.save()
    return c


def add_collection(user_name, recipe_title):
    u = UserProfile.objects.get(user__username=user_name)
    r = Recipe.objects.get(title=recipe_title)
    u.collections.add(r)
    return u


if __name__ == '__main__':
    print('Starting fooddance population script...')
    populate()