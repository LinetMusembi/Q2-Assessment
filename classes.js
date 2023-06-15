// 1.# **Ancestral Stories:** In many African cultures, the art of storytelling is passed
// # down from generation to generation. Imagine you're creating an application that
// # records these oral stories and translates them into different languages. The
// # stories vary by length, moral lessons, and the age group they are intended for.
// # Think about how you would model `Story`, `StoryTeller`, and `Translator`
// # objects, and how inheritance might come into play if there are different types of
// # stories or storytellers.

// # input....Length of the story,the moral lesson in the story,and the age group the story is intended for.
// # outout....the story,different storytellers and a translator.
// # Process...create a class Story,give it attributes length,lesson and age.Create different methods.

class Story {
    constructor(length, lesson, ageGroup) {
      this.length = length;
      this.lesson = lesson;
      this.ageGroup = ageGroup;
    }

  
    start() {
      return "Long long time age.." + this.lesson + " that was " + this.length + " long. It was intended for " + this.ageGroup + " age group.";
    }
  
    addTranslator(translator) {
      this.translator = translator;
    }
  
    translateStory(language) {
      if (this.translator) {
        return this.translator.translate(this.lesson, language);
      } else {
        return "Translator not available.";
      }
    }
  }
  class StoryTeller {
    constructor(name, language) {
      this.name = name;
      this.language = language;
    }
  
    introduce() {
      return "Hi, my name is " + this.name + " and I tell stories in " + this.language + ".";
    }
}
  
  class AfricanStoryTeller extends StoryTeller {
    constructor(name, language, region) {
      super(name, language);
      this.region = region;
    }
  
    introduce() {
      return "Hi, my name is " + this.name + " and I come from " + this.region + " and my stories are in " + this.language + ".";
    }
  }
  
  class Translator {
    translate(text, language) {
      return "Translation of " + text + " into " + language + " is ongoing.";
    }
  }

  
  const story1 = new Story(10, "the importance of sharing", "children");
  console.log(story1.tellStory()); 

//   # # 2.**African Cuisine:** You're creating a recipe app specifically for African cuisine.
//   # The app needs to handle recipes from different African countries, each with its
//   # unique ingredients, preparation time, cooking method, and nutritional
//   # information. Consider creating a `Recipe` class, and think about how you might
//   # create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
//   # `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
//   # methods.
  
//   # input....ingredients,preparation-time,cooking-method,nutritional-information
//   # Output...subclasses for(MoroccanRecipe,EthiopianRecipe and NigerianRecipe),each with its own properties 
//   #class Story {
class Recipe{ 
    constructor(ingredients, time, procedurenutrients) {
        this.ingredients = ingredients
        this.time = time
        this.procedurenutrients = procedurenutrients
      }
    }
    

