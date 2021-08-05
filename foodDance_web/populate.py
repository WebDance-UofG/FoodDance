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
        {'username': 'diablo', 'password': 'test123', 'email': 'diablo@test.com', 'image': 'avatars/diablo.png'},
        {'username': 'Augenstern', 'password': 'test123', 'email': 'Augenstern@test.com', 'image': 'avatars/augenstern.jpg'},
        {'username': 'yuuki', 'password': 'test123', 'email': 'yuuki@test.com', 'image': 'avatars/yuuki.jpg'},
        {'username': 'flechazo', 'password': 'test123', 'email': 'flechazo@test.com', 'image': 'avatars/flechazo.jpg'},
        {'username': 'espoir', 'password': 'test123', 'email': 'espoir@test.com', 'image': 'avatars/espoir.jpg'},
    ]

    recipes = [
        {'title': 'Floral Yoghurt Biscuits',
         'author': 'Augenstern',
         'image': 'recipes/floral-yoghurt-biscuits.jpg',
         'overview':
            "This recipe is a sugar-free version that you can make for your baby, it's melt-in-your-mouth, crispy and tasty and is suitable for all ages. ",
         'duration': 90,
         'budget': 5,
         'difficulty': 5,
         'materials': [
             {'ingredient': 'egg', 'weight': '50g'},
             {'ingredient': 'Powdered milk (for yolk)', 'weight': '6g'},
             {'ingredient': 'Powdered milk (for egg white)', 'weight': '10g'},
             {'ingredient': 'yoghurt', 'weight': '16g'},
             {'ingredient': 'Cornstarch', 'weight': '6g'},
             {'ingredient': 'lemon juice', 'weight': '10g'},
         ],
         'steps': [
             {'content': 'Separate the egg yolks from the whites. Chill the egg whites in the fridge until ice appears on the side of the bowl, as this will make them easier to whip.'},
             {'content': 'Whip the egg yolks until they are lighter in colour. Add 6g of milk powder and mix well until there are no particles.'},
             {'content': 'Put a laminating bag over the cups and use a silicone spatula to put the egg yolks into the bag. Cut out a small slit in the bag and use a spatula to drive the yolk downwards and wrap the bag around your index finger, holding the bag in the palm of your hand.'},
             {'content': 'Line a baking tray in advance with greaseproof paper and squeeze out pea-sized balls. Be careful to leave enough space so that the egg whites do not stick together when you squeeze them later. Bake in a preheated (100°C) oven for 20 minutes.'},
             {'content': 'Add 10 g of milk powder to the yoghurt, this is where the milk powder used for the egg white part was written about earlier. Stir well until the yoghurt batter is grain-free and set aside.'},
             {'image': 'floral-yoghurt-biscuits_1.jpg',
                 'content': 'Squeeze 2-3 drops of lemon juice into the egg whites and beat to make large fish-eye bubbles. Add 6g of corn starch and continue to beat. Beat stiffly until firm with small sharp hooks.'},
             {'image': 'floral-yoghurt-biscuits_2.jpg',
                 'content': 'Add the yoghurt batter to the whipped egg whites, mix well and put into a laminating bag. Remove the baked egg yolks and use the bag containing the egg whites to squeeze 5 balls around the yolks one week to act as petals.'},
             {'content': 'Bake in the oven at 100°C for about 40 minutes.'},
                         
         ],
         'comments': [
             {'user': 'diablo', 'rating': 3, 'content': "It's so cute, I can't even bear to eat it."},
             {'user': 'flechazo', 'rating': 5, 'content': "It's cute but it's a little bit hard for me."},
             {'user': 'yuuki', 'rating': 4, 'content': "All of my families love it."},
         ]
         },
         
        {'title': 'Red Bean Jicama',
         'author': 'flechazo',
         'image': 'recipes/red-bean-jicama.jpg',
         'overview':
            "Oven free! Soft and creamy Japanese sweet bean jicama, perfect as a snack for kids, super cute!",
         'duration': 90,
         'budget': 20,
         'difficulty': 5,
         'materials': [
             {'ingredient': 'milk', 'weight': '160g'},
             {'ingredient': 'sugar', 'weight': '45g'},
             {'ingredient': 'corn starch', 'weight': '30g'},
             {'ingredient': 'glutinous rice flour', 'weight': '100g'},
             {'ingredient': 'butter', 'weight': '15g'},
             {'ingredient': 'bean paste', 'weight': '135g'},
             {'ingredient': 'melted chocolate', 'weight': '20g'},
             {'ingredient': 'leaves(mine were cherry leaves)', 'weight': '20g'},
         ],
         'steps': [
             {'content': '160g milk mix with 45g sugar, add 100g glutinous rice flour/30g corn starch, mix together.'},
             {'content': 'Sift the mixture through a sieve and pour into a container.'},
             {'content': 'Wrap in cling film, make a few holes to vent the air and steam for 25-30 minutes. During the steaming process, fry some flour, divide 135g of bean paste into 9 portions, 15g per portion, and knead into small balls. When the batter is steamed add 15g of butter while it is still hot.'},
             {'content': 'Toss and mix until not too sticky, then knead into a dough.'},
             {'content': 'Repeat a few times, divide into 35g portions, 9 portions in total (use the rest for the five senses), roll out into a round cake, put the bean paste on top, fold in half and knead three small balls to make the nose and ears.'},
             {'content': 'Wrap the leaves, cut off the excess and use the melted chocolate to draw expressions on them.'},            
         ],
         'comments': [
             {'user': 'Augenstern', 'rating': 5, 'content': "It's so cute, I can't even bear to eat it."},
             {'user': 'espoir', 'rating': 3, 'content': "It's cute but it's a little bit hard for me."},
             {'user': 'yuuki', 'rating': 4, 'content': "Love it but it takes too much time."},
         ]
         },
         
        {'title': 'Paella mixta',
         'author': 'Augenstern',
         'image': 'recipes/paella-mixta.jpg',
         'overview':
            "Try our version of paella, made with a combination of meat and seafood. With king prawns, mussels, chorizo" 
            "and chicken, every forkful is a treat that's reminiscent of Spanish holidays",
         'duration': 75,
         'budget': 20,
         'difficulty': 5,
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
             {'user': 'flechazo', 'rating': 2, 'content':"It costs too much time"},
             {'user': 'espoir', 'rating': 1, 'content':"It is tooooo diffcult! give a easy vesion plz"},
             {'user': 'diablo', 'rating': 5, 'content':"Super yummy! totally worth my time"},
             {'user': 'yuuki', 'rating': 4, 'content':"will do this again!"},
         ]
         },
    
        {'title': 'Vegan Cheesecake',
         'author': 'diablo',
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
             {'user': 'Augenstern', 'rating': 3, 'content': "I’d really like some ca-me:"},
             {'user': 'yuuki', 'rating': 2, 'content': "This cake is absolutely perfect it's so soft and delicious wow just wow"},
             {'user': 'Augenstern', 'rating': 5, 'content': "i could really go for some cake me asf:"},
         ]
         },
         
        {'title': 'Ramen noodle',
         'author': 'Augenstern',
         'image': 'recipes/ramen-noodle.jpg',
         'overview':
            "Use chicken, noodles, spinach, sweetcorn and eggs to make this moreish Japanese noodle soup, for when you crave something comforting yet light and wholesome.",
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
             {'user': 'diablo', 'rating': 2, 'content':"It's easy...just not tasty"},
             {'user': 'espoir', 'rating': 3, 'content':"40 pounds cheaper than a high street chain wag"},
         ]
         },
         
        {'title': 'Beef curry',
         'author': 'yuuki',
         'image': 'recipes/beef-curry.jpg',
         'overview':
            "Make our easy beef curry and serve with a hunk of naan bread to mop up the delicious juices. If you prefer it less spicy, simply add less chilli powder.",
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
             {'user': 'Augenstern', 'rating':3 , 'content':"Looks great but what do you season the beef with please?"},
             {'user': 'espoir', 'rating':4 , 'content':"I've made this three times in the last couple of months. It's delicious and everyone ate it."},
             {'user': 'flechazo', 'rating':1 , 'content':"Cooked with chicken, really horrible..."},
         ]
         },
         
        {'title': 'Chicken Casserole',
         'author': 'diablo',
         'image': 'recipes/chicken-casserole.jpg',
         'overview':
            "An easy chicken casserole recipe should be in every cook's little black book and this one will go down well with all of the family. Serve with mashed or boiled potatoes, or rice."
            "Each serving provides 425 kcal, 48g protein, 13g carbohydrates (of which 7.5g sugars), 19g fat (of which 5g saturates), 5g fibre and 2.4g salt.",
         'duration': 90,
         'budget': 20,
         'difficulty': 4,
         'materials': [
             {'ingredient': 'chicken thighs ', 'weight': '850g'},
             {'ingredient': 'olive or sunflower oil', 'weight': '50g'},
             {'ingredient': ' onion', 'weight': '70g'},
             {'ingredient': 'rashers smoked back bacon', 'weight': '100g'},
             {'ingredient': 'mushroom', 'weight': '150g'},
             {'ingredient': 'carrots', 'weight': '135g'},
             {'ingredient': 'plain flour', 'weight': '20g'},
             {'ingredient': 'fresh thyme leaves', 'weight': '50g'},
             {'ingredient': ' hot chicken stock', 'weight': '500g'},
         ],
         'steps': [
             {'content': 'Preheat the oven 190C/170C Fan/Gas 5. Season the chicken thighs all over with a little salt and lots of black pepper.'},
             {'content': 'Heat the oil in a large non-stick frying pan over a medium heat and fry the chicken for 7–8 minutes, skin-side down, or until the skin is nicely browned. Turn and cook on the other side for 3 minutes more. Transfer to a plate.'},
             {'content': 'Return the pan to the heat and add the onion, bacon and mushrooms. Fry over a medium-high heat for 4–5 minutes, or until lightly browned, stirring regularly. Tip into a medium, lidded oven-safe pan or casserole. Add the carrots and flour and toss together well.'},
             {'content': 'Sprinkle with the thyme, then pour in the stock, a little at a time, stirring well between each addition. Add the chicken pieces back to the pan and bring to a gentle simmer. Cover the pan with a lid.'},
             {'content': 'Place in the oven and cook for 45 minutes. Take out of the oven and stir in the leeks. Return to the oven for a further 15 minutes, or until the chicken and leeks are tender and the sauce has thickened. Serve.'},              
         ],
         'comments': [
             {'user': 'Augenstern', 'rating': 5, 'content': "It's tasty."},
             {'user': 'espoir', 'rating': 3, 'content': "It's cute but it's a little bit hard for me."},
             {'user': 'flechazo', 'rating': 4, 'content': "Love it, it's really suitable for a family party."},
         ]
         },
         
        {'title': 'Roast chicken',
         'author': 'yuuki',
         'image': 'recipes/roast-chicken.jpg',
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
             {'user': 'Augenstern', 'rating': 4, 'content':"Super easy to follow! Thanks for sharing!"},
             {'user': 'espoir', 'rating': 3, 'content':"Winter smell, got hugry already ;-)"},
             {'user': 'diablo', 'rating': 2, 'content':"Got roasted..."},
             {'user': 'Augenstern', 'rating': 4, 'content':"I made this for my dinner. will do it again!"},
         ]
         },
         
        {'title': 'Sponge pudding',
         'author': 'diablo',
         'image': 'recipes/sponge-pudding.jpg',
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
             {'user': 'diablo', 'rating': 1, 'content':"Too much steps"},
             {'user': 'flechazo', 'rating': 2, 'content':"Very sour, is it just me..."},
             {'user': 'yuuki', 'rating': 4, 'content':"Yummy!"},
             {'user': 'Augenstern', 'rating': 1, 'content':"Should not mix it directly"},
         ]
         },
              
        {'title': 'Sauteed Cauliflower with Mushrooms',
         'author': 'Augenstern',
         'image': 'recipes/sauteed-cauliflower-with-mushrooms.jpg',
         'overview':
            "Sauteed cauliflower with mushroom is rich in flavour, nutritious and delicious, perfect for family dinners.",
         'duration': 30,
         'budget': 7,
         'difficulty': 4,
         'materials': [
             {'ingredient': 'unsalted butter', 'weight': '60g'},
             {'ingredient': 'onion', 'weight': '75g'},
             {'ingredient': 'cauliflower', 'weight': '300g'},
             {'ingredient': 'mushrooms', 'weight': '500g'},
             {'ingredient': 'parsley', 'weight': '50g'},
             {'ingredient': 'Garlic', 'weight': '50g'},
         ],
         'steps': [
             {'image': 'sauteed-cauliflower-with-mushrooms_1.jpg',
                 'content': 'Melt the butter over medium-low heat, add the olive oil; add the chopped onion and soften, about 2-3 minutes; add the mushrooms and fry for 3-4 minutes.'},
             {'image': 'sauteed-cauliflower-with-mushrooms_2.jpg',
                 'content': 'Add the head of cauliflower (process the cauliflower by cutting off the stem part) and sauté until the edges of the cauliflower begin to turn golden brown, about 8 minutes.'},
             {'image': 'sauteed-cauliflower-with-mushrooms_3.jpg',
                 'content': 'Pour in the stock and cook for 2 minutes, then add the garlic, thyme and parsley and stir-fry for about 1 minute.'},
             {'content': 'Taste before serving and add salt or no salt to taste, as some stock may have salt in it; pepper and serve with aromas.'},
         ],
         'comments': [
             {'user': 'yuuki', 'rating': 3, 'content': "It seems interesting, I will try it later."},
             {'user': 'flechazo', 'rating': 5, 'content': "I follow this recipe and cook for my parents last week, they said it's over imagine!"},
             {'user': 'espoir', 'rating': 4, 'content': "I've fall in love with it, it's very decilious."},
         ]
         },

        {'title': 'Tortilla pizza',
         'author': 'Augenstern',
         'image': 'recipes/tortilla-pizza.jpg',
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
             {'user': 'yuuki', 'rating': 3, 'content': "love this recipe! helps me alot"},
             {'user': 'flechazo', 'rating': 2, 'content': "Why do I got a half-raw pasta? I followed all the steps"},
             {'user': 'flechazo', 'rating': 1, 'content': "Waste my time, juice of tomatoes makes it super wet..."},
             {'user': 'diablo', 'rating': 4, 'content': "Good recipe, add tomatoes making it even delicious"},
         ]
         },
         
        {'title': 'Beef stew',
         'author': 'yuuki',
         'image': 'recipes/beef-stew.jpg',
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
             {'user': 'flechazo', 'rating': 5, 'content':"Absolutely delicious! So easy to make and everyone loves it."},
             {'user': 'Augenstern', 'rating': 1, 'content':"Too time consuming to make it second time"},
             {'user': 'espoir', 'rating': 5, 'content':"It's my first time cooking beef and I followed this recipe. Too delicious to believe it's my own work!"},
         ]
         },
         
        {'title': 'Chocolate cake',
         'author': 'diablo',
         'image': 'recipes/chocolate-cake.jpg',
         'overview':
            "Need a guaranteed crowd-pleasing cake that's easy to make?"
            "This super-squidgy chocolate fudge cake with smooth icing is an instant baking win.",
         'duration': 45,
         'budget': 25,
         'difficulty': 3,
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
             {'user': 'Augenstern', 'rating': 5, 'content':"Cannot wait to have one"},
             {'user': 'yuuki', 'rating': 2, 'content':"My daughter really loves it! Fab recipe"},
             {'user': 'espoir', 'rating': 1, 'content':"Hard to follow..."},
         ]
         },
         
        {'title': 'Poke Bowl',
         'author': 'yuuki',
         'image': 'recipes/poke-bowl.jpg',
         'overview':
            "Poke bowl is healthy, low fat and delicious. Recommended for those who are in the process of fat loss or fitness."
            "You can put in whatever ingredients you feel are tasty and healthy, exactly as you like.",
         'duration': 45,
         'budget': 15,
         'difficulty': 3,
         'materials': [
             {'ingredient': 'avocado', 'weight': '100g'},
             {'ingredient': 'onion', 'weight': '75g'},
             {'ingredient': 'egg', 'weight': '25g'},
             {'ingredient': 'small tomatoes', 'weight': '120g'},
             {'ingredient': 'corn kernels', 'weight': '75g'},
             {'ingredient': 'pickles', 'weight': '50g'},
             {'ingredient': 'crab sticks', 'weight': '30g'},
             {'ingredient': 'Rice and quinoa', 'weight': '120g'},
         ],
         'steps': [
             {'image': 'poke-bowl_1.jpg',
                 'content': 'Steam the rice and quinoa in a 1:1 ratio and sprinkle with some aromatic pine while it is still hot.'},
             {'image': 'poke-bowl_2.jpg',
                 'content': 'Soul vinaigrette: 2 tbsp olive oil, 2 tbsp apple cider vinegar (or lemon juice), salt, a little black pepper, 1 tbsp honey and 2 tbsp soy sauce'},
             {'image': 'poke-bowl_3.jpg',
                 'content': 'Cut the ingredients into small pieces and spread them on top of the quinoa rice, add a poached egg in the middle, poke the poached egg before eating, pour the sauce in and mix it well into the rice, a bowl of high protein, low fat poached rice is ready, you definitely deserve it!'},
         ],
         'comments': [
             {'user': 'diablo', 'rating': 4, 'content': "It's really easy and yummy, I have already recommend this to all my friends."},
             {'user': 'flechazo', 'rating': 5, 'content': "I have tries poke bowl before, but this pairing was so much better than the ones I've tried before and the sauce was really tasty."},
             {'user': 'Augenstern', 'rating': 4, 'content': "Have tried, great."},
         ]
         },
         
        {'title': 'Seafood pasta',
         'author': 'Augenstern',
         'image': 'recipes/seafood-pasta.jpg',
         'overview':
            "Make a low in fat, satisfying dish in minutes – ideal for Friday nights",
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
             {'user': 'diablo', 'rating': 5, 'content':"Really liked this , made it for the family, kids loved it"},
             {'user': 'yuuki', 'rating': 3, 'content':"Cooked perfectly. Will definitely do this again!"},
             {'user': 'flechazo', 'rating': 4, 'content':"Quick,healthy and delicious! Fab recipe!"},
             {'user': 'flechazo', 'rating': 4, 'content':"Can you add cream, or creme fraiche to make it a creamy sauce?"},
             {'user': 'espoir', 'rating': 1, 'content':"Worst thing I’ve ever spent my time and money on."},
         ]
         },

        {'title': 'Volcanic Lava Egg',
         'author': 'diablo',
         'image': 'recipes/volcanic-lava-egg.jpg',
         'overview':
            "Today I'm giving you a volcano that will erupt with deliciousness and fill your stomach.",
         'duration': 45,
         'budget': 7,
         'difficulty': 2,
         'materials': [
             {'ingredient': 'potato', 'weight': '100g'},
             {'ingredient': 'bacon', 'weight': '135g'},
             {'ingredient': 'cheese', 'weight': '150g'},
             {'ingredient': 'egg', 'weight': '75g'},
             {'ingredient': 'chopped green onion', 'weight': '30g'},
         ],
         'steps': [
             {'image': 'volcanic-lava-egg_1.jpg',
                 'content': 'Peel the medium potatoes and hollow them out with a ball peeler to create the shape of a "volcano".'},
             {'image': 'volcanic-lava-egg_2.jpg',
                 'content': 'Roll the potatoes in bacon, secure with a toothpick and bake in an oven at 200°C for 40 minutes.'},
             {'content': 'Remove the potatoes from the oven and leave until they are not too hot. Add half a slice of cheese, 1 egg (I used a sterile langoustine egg) and chopped spring onion in the middle of the potatoes, in order of preference. Bake in a 170°C oven for 10 minutes, or longer to 15 minutes if you like the eggs fully cooked.'},                 
         ],
         'comments': [
             {'user': 'Augenstern', 'rating': 5, 'content': "It's so yummy! I've tried many times, with great success, every time."},
             {'user': 'espoir', 'rating': 5, 'content': "Love it! If you don't want to carve the potatoes you can just put the ingredients together."},
             {'user': 'flechazo', 'rating': 4, 'content': "Shap the potatoes is too hard! But it's really tasty."},
         ]
         },
         
        {'title': 'Low Fat North African Egg',
         'author': 'espoir',
         'image': 'recipes/low-fat-north-african-egg.jpg',
         'overview':
            "Originating in the Mediterranean, the North African egg is an exotic dish with a special flavour, rich in nutrients and low in fat and calories ~ it can be served for any meal, breakfast, lunch or dinner.",
         'duration': 40,
         'budget': 10,
         'difficulty': 2,
         'materials': [
             {'ingredient': 'onion', 'weight': '40g'},
             {'ingredient': 'tomatoes', 'weight': '300g'},
             {'ingredient': 'eggs', 'weight': '100g'},
             {'ingredient': 'mushrooms', 'weight': '100g'},
             {'ingredient': 'Black pepper', 'weight': '20g'},
             {'ingredient': 'ham', 'weight': '135g'},
         ],
         'steps': [
             {'image': 'low-fat-north-african-egg_1.jpg',
                 'content': 'Prepare the ingredients, slice the mushrooms, beat the onions in a cooking machine and peel and dice the tomatoes.'},
             {'image': 'low-fat-north-african-egg_2.jpg',
                 'content': 'Add the butter to the pan and heat it evenly, then stir-fry the onions until they are transparent (protect your eyes, good quality onions are really spicy)'},
             {'image': 'low-fat-north-african-egg_3.jpg',
                 'content': 'Add the diced tomatoes and stir-fry to get the juice ~tips: if you like to be delicate. You can divide half of the tomatoes into tomato paste and then pour it back into the pot to cook together. When the tomatoes are juiced, add the sliced mushrooms and shredded ham.'},
             {'image': 'low-fat-north-african-egg_4.jpg',
                 'content': 'Finally, reduce the heat to medium, dig three holes in the tomatoes and simmer the eggs in.'},
             {'image': 'low-fat-north-african-egg_5.jpg',
                 'content': 'Done!'},           
         ],
         'comments': [
             {'user': 'flechazo', 'rating': 3, 'content': "Love it but it takes too much time to prepare the materials."},
             {'user': 'yuuki', 'rating': 1, 'content': "I don's like the taste of mushroom."},
             {'user': 'diablo', 'rating': 5, 'content': "It's really easy and tasty!."},
         ]
         },

        {'title': 'Beef Donburi',
         'author': 'flechazo',
         'image': 'recipes/beef-donburi.jpg',
         'overview':
            "Tender beef in a rich sauce, served with a raw egg. Serve with a drizzle of Japanese soy sauce and you've got a delicious bowl of beef donburi! Super healing!",
         'duration': 30,
         'budget': 14,
         'difficulty': 2,
         'materials': [
             {'ingredient': 'beef', 'weight': '200g'},
             {'ingredient': 'sterile egg', 'weight': '30g'},
             {'ingredient': 'onion', 'weight': '74g'},
             {'ingredient': 'carrot', 'weight': '50g'},
             {'ingredient': 'green onion', 'weight': '15g'},
             {'ingredient': 'rice', 'weight': '100g'},
             {'ingredient': 'butter', 'weight': '15g'},
         ],
         'steps': [
             {'image': 'beef-donburi_1.jpg',
                 'content': 'Shred the onion, no need to be too fine. Shredded carrots. Make the sauce, a spoonful of soy sauce, half a spoonful of soy sauce, a spoonful of wine, a spoonful of oyster sauce, half a spoonful of sugar, half a spoonful of cornstarch, a pinch of salt, half a bowl of water and a pinch of cracked black pepper.'},
             {'image': 'beef-donburi_2.jpg',
                 'content': 'Stir-fry the onions and carrots to soften first. Add the fatty beef and stir-fry until the beef is browned, add the sauce and stir-fry, then quickly set aside.'},
             {'image': 'beef-donburi_3.jpg',
                 'content': 'Carefully place the loose egg on top of the hot rice and lay the fatty beef on top. Sprinkle with some chopped spring onion and chopped seaweed and sesame seeds.'},
                         
         ],
         'comments': [
             {'user': 'Augenstern', 'rating': 5, 'content': "It's much easier than i thouht and very tasty"},
             {'user': 'espoir', 'rating': 4, 'content': "Very tasty, just hard to get the timing right for the omelette."},
             {'user': 'diablo', 'rating': 4, 'content': "Love it!"},
         ]
         },

        {'title': 'Aloo chaat',
         'author': 'Augenstern',
         'image': 'recipes/aloo-chaat.jpg',
         'overview':
            "Aloo chaat is a combination of different flavours all in one dish. It reminds me of childhood with my friends and is a great sharing dish.",
         'duration': 30,
         'budget': 20,
         'difficulty': 2,
         'materials': [
             {'ingredient': 'potato', 'weight': '600g'},
             {'ingredient': 'cumin', 'weight': '10g'},
             {'ingredient': 'coriander', 'weight': '10g'},
             {'ingredient': 'fennel seend', 'weight': '10g'},
             {'ingredient': 'chaat masala', 'weight': '20g'},
             {'ingredient': 'chilli powder', 'weight': '10g'},
             {'ingredient': 'fresh coriander', 'weight': '15g'},
             {'ingredient': 'pomegranate', 'weight': '50g'},
             {'ingredient': 'lemon juice', 'weight': '15g'},
             {'ingredient': 'caster sugar', 'weight': '10g'},
             {'ingredient': 'milk', 'weight': '20g'},
             {'ingredient': 'tamarind chutney', 'weight': '60g'},
             {'ingredient': 'haldiram bhujia', 'weight': '40g'},
             {'ingredient': 'salt', 'weight': '5g'},
         ],
         'steps': [
             {'content': 'To make the aloo chaat, cook the potatoes in a saucepan of lightly salted boiling water until just cooked through. Drain and leave to cool. Put the cooled potatoes, all the spices (except the cumin seeds), 10g/⅓oz fresh coriander and 35g/1¼oz pomegranate seeds in a large bowl with the chillies, lemon juice and ½ tsp salt. Mix together and set aside.'},
             {'content':'Put the yoghurt, sugar, cumin seeds and milk in a bowl and whisk together.'},
             {'content':'To make the mint and coriander chutney, place all of the ingredients together with 20–30ml/¾–1fl oz water in a food processor or blender and blend until smooth.'},
             {'content':'Place the potato mixture on a large serving plate. Spoon the yoghurt mixture over the potatoes. Top with 4 teaspoons of tamarind chutney and 4 teaspoons of mint and coriander chutney. Sprinkle with the bhujia, remaining pomegranate seeds and fresh coriander, then spoon over 1 teaspoon of mint and coriander chutney and 2 teaspoons of tamarind chutney. Serve for everyone to share.'},            
         ],
         'comments': [
             {'user': 'yuuki', 'rating': 3, 'content': "It's good."},
             {'user': 'diablo', 'rating': 3, 'content': "I've tried but i'm not that like it."},
             {'user': 'flechazo', 'rating': 4, 'content': "Love it!"},
         ]
         },
         
        {'title': 'Steamed Buns',
         'author': 'diablo',
         'image': 'recipes/steamed-buns.jpg',
         'overview':
            "A very simple and easy to prepare steamed bun, suitable for children.",
         'duration': 20,
         'budget': 5,
         'difficulty': 2,
         'materials': [
             {'ingredient': 'potato', 'weight': '100g'},
             {'ingredient': 'carrot', 'weight': '100g'},
             {'ingredient': 'green pepper', 'weight': '75g'},
             {'ingredient': 'ham sausage', 'weight': '150g'},
             {'ingredient': 'eggs', 'weight': '75g'},
             {'ingredient': 'Dumpling skin', 'weight': '100g'},
         ],
         'steps': [
             {'image': 'recipes/steamed-buns_1.jpg',
                 'content': 'Shredded carrots and shredded potatoes. Add the shredded potatoes, carrots and peppers to a pot of boiling water, blanch for 30 seconds and then remove from the pot.'},
             {'image': 'recipes/steamed-buns_2.jpg',
                 'content': 'Mix the shredded potatoes, shredded carrots, shredded green pepper, shredded ham, egg, salt and soy sauce.'},
             {'image': 'recipes/steamed-buns_3.jpg',
                 'content': 'Roll out the dumpling skin thinly. Put the filling into the dumpling skin, apply a layer of water around the skin and pinch tightly.'},
             {'image': 'recipes/steamed-buns_4.jpg',
                 'content': 'Place in a steamer and steam for 8 minutes on high heat. After 8 minutes, you can enjoy it beautifully.'},
         ],
         'comments': [
             {'user': 'flechazo', 'rating': 3, 'content': "It seems interesting, I will try it later."},
             {'user': 'yuuki', 'rating': 1, 'content': "I don't really like it."},
             {'user': 'Augenstern', 'rating': 5, 'content': "I've fall in love with it, it's simple and also very decilious"},
         ]
         }, 
         
        {'title': 'Rice pudding',
         'author': 'diablo',
         'image': 'recipes/rice-pudding.jpg',
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
             {'user': 'espoir', 'rating': 4, 'content':"Easy and yummy!"},
             {'user': 'yuuki', 'rating': 3, 'content':"best dinner disert"},
         ]
         }, 
         
        {'title': 'Americano',
         'author': 'yuuki',
         'image': 'recipes/americano.jpg',
         'overview':
            "An Americano mixes Campari and sweet red vermouth, topped up with soda water. It makes a refreshing aperitif, perfect for a hot summer’s day.",
         'duration': 20,
         'budget': 5,
         'difficulty': 1,
         'materials': [
             {'ingredient': 'campari', 'weight': '30g'},
             {'ingredient': 'sweet red vermouth', 'weight': '30g'},
             {'ingredient': 'handful ice', 'weight': '100g'},
             {'ingredient': 'soda water', 'weight': '100g'},
             {'ingredient': 'orige slice', 'weight': '15g'},
         ],
         'steps': [
             {'content': 'Pour the Campari and sweet vermouth into a collins glass full of ice.'},
             {'content': 'Top the mixture with soda water and give it a gentle little stir to combine all the ingredients. Garnish with an orange slice or two if using.'},             
         ],
         'comments': [
             {'user': 'Augenstern', 'rating': 5, 'content': "Yummy!"},
             {'user': 'espoir', 'rating': 3, 'content': "Prety good"},
             {'user': 'flechazo', 'rating': 4, 'content': "I like it, it's very easy."},
         ]
         },

        {'title': 'Avocado and Shrimp Sandwich with Egg Cream',
         'author': 'yuuki',
         'image': 'recipes/avocado-and-shrimp-sandwich-with-egg-cream.jpg',
         'overview':
            "A breakfast classic, served with coffee, you can't get enough of it!",
         'duration': 20,
         'budget': 12,
         'difficulty': 1,
         'materials': [
             {'ingredient': 'avocado', 'weight': '60g'},
             {'ingredient': 'egg', 'weight': '75g'},
             {'ingredient': 'toast', 'weight': '100g'},
             {'ingredient': 'shrimp', 'weight': '70g'},
             {'ingredient': 'lemon juice', 'weight': '5g'},
             {'ingredient': 'black pepper', 'weight': '5g'},
         ],
         'steps': [
             {'image': 'recipes/avocado-and-shrimp-sandwich-with-egg-cream_1.jpg',
                 'content': 'Scoop out the flesh of the avocado, add black pepper and lemon juice and press into an avocado puree.'},
             {'image': 'recipes/avocado-and-shrimp-sandwich-with-egg-cream_2.jpg',
                 'content': 'Fry the shrimps, beat the eggs with black pepper and a pinch of salt and make a smooth egg.'},
             {'content': 'Spread the toast with the mashed avocado, the egg and the shrimps and finish with a sprinkling of chopped parsley.'},            
         ],
         'comments': [
             {'user': 'Augenstern', 'rating': 5, 'content': "It's easy and yummy!"},
             {'user': 'espoir', 'rating': 3, 'content': "Prety good."},
             {'user': 'flechazo', 'rating': 4, 'content': "Love it! It's more suitable to serve with milk."},
         ]
         },
         
        {'title': 'Oatmeal and Avocado Tart',
         'author': 'espoir',
         'image': 'recipes/oatmeal-and-avocado-tart.jpg',
         'overview':
            "A zero-difficulty, high-value, super-fast fat-reducing dessert is here! No oil and no sugar to eat without the burden.",
         'duration': 15,
         'budget': 10,
         'difficulty': 1,
         'materials': [
             {'ingredient': 'avocado', 'weight': '75g'},
             {'ingredient': 'milk', 'weight': '200g'},
             {'ingredient': 'instant oats', 'weight': '120g'},
             {'ingredient': 'banana', 'weight': '100g'},
             {'ingredient': 'giletine flake', 'weight': '5g'},
         ],
         'steps': [
             {'content': 'Mash the bananas and mix well with the oats. Leave to stand for a while to allow the oats to absorb all the water from the bananas.'},
             {'image': 'oatmeal-and-avocado-tart_1.jpg',
                 'content': 'Grease a tart pan (8 inch tart pan) and spread the oats into the mixture. Bake in the preheated oven at 180°C for 10 minutes to set.'},
             {'content': 'Puree the avocado with the milk and add the softened giardiniera slices to the pan and mix well.'},
             {'image': 'oatmeal-and-avocado-tart_2.jpg',
                 'content': 'Pour through a sieve into the oatmeal tart shell and chill in the fridge overnight.'},       
         ],
         'comments': [
             {'user': 'diablo', 'rating': 5, 'content': "It's so cute, I can't even bear to eat it."},
             {'user': 'yuuki', 'rating': 4, 'content': "It's really easy and don't need much time."},
             {'user': 'flechazo', 'rating': 4, 'content': "Yummy!"},
         ]
         },         
    ]

    collections = [
        {
            'user': 'diablo',
                'recipes': ['Paella mixta', 'Beef curry', 'Seafood pasta',
                            'Poke Bowl', 'Red Bean Jicama'],
        },
        {
            'user': 'Augenstern', 'recipes': ['Vegan Cheesecake', 'Low Fat North African Egg',
                                              'Volcanic Lava Egg', 'Avocado and Shrimp Sandwich with Egg Cream' ]

        },
        {
            'user': 'yuuki', 'recipes': ['Roast chicken', 'Floral Yoghurt Biscuits', 'Beef Donburi', 'Steamed Buns']
        },
        {
            'user': 'flechazo', 'recipes': ['Vegan Cheesecake', 'Beef stew']
        },
        {
            'user': 'espoir', 'recipes': ['Sponge pudding', 'Chocolate cake', 'Rice pudding']
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
        for recipe in collection['recipes']:
            u = add_collection(collection['user'], recipe)
            print(f"- {collection['user']} collect {recipe}")


def add_user(username, password, email, image=None):
    user = User.objects.get_or_create(username=username, email=email)[0]
    user.set_password(password)

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
    time.sleep(0.2)
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